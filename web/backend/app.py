from flask import Flask, request
from flask_cors import CORS
from web.backend.model import WeatherRequest, WeatherResponse, DailyEnergy
from web.backend.api import WeatherAPI
import json
import calendar
from datetime import datetime, timedelta
import pandas as pd
import sys, os.path
# cleaning_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# print(cleaning_dir)
# sys.path.append(cleaning_dir)
from cleaning import preprocess_solar
from cleaning import preprocess_wind
import analysis.variables as v
import pickle

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def body(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

@app.route("/", methods=['POST'])
@body(WeatherRequest)
def get_energy(body):
    # Getting weather data given a coordinate an starting and ending month/year
    # We can only request the api for data for one month tops (so 1 year needs 12 requests to the API)
    api = WeatherAPI(body.coordinate.lat, body.coordinate.lon)
    month, year = (int(elem) for elem in body.startMonthYear.split('/'))
    time = datetime(year, month, 1)
    month, year = (int(elem) for elem in body.endMonthYear.split('/'))
    timeend = datetime(year, month, calendar.monthrange(year, month)[1], hour=23)

    # Joining the data in a pandas Series
    items = []
    while time < timeend:
        farm = body.farmConfiguration.__dict__
        weather = api.get_weather_data(time)
        item = {
            'lat': body.coordinate.lat,
            'lon': body.coordinate.lon,
            'time': time
        }
        items.append({**farm, **weather, **item})
        time += timedelta(hours=1)
    df = pd.DataFrame(items)

    # Calling preprocessing step
    if body.solar:
        processed_df = preprocess_solar.clean_data(df)
        processed_df = processed_df[v.solar_x]
    else:
        processed_df = preprocess_wind.clean_data(df)
    
    # Calling predict for all the hours
    path = os.path.join('analysis', 'models', 'xgboost_solar.dat')
    model = pickle.load(open(path, "rb"))
    # TODO: is the order of the columns the same that is been trained?
    df['energy'] = model.predict(processed_df.values)

    # Aggregating data by day
    df = df[['time', 'energy']]
    df.set_index('time', inplace=True)
    df = df.resample('D').sum()
    # Return data
    items = WeatherResponse()
    for time, row in df.iterrows():
        energy = row['energy']
        items.data.append(DailyEnergy(time.strftime('%d/%m/%Y'), f'{energy:.3f}').__dict__)
    return json.dumps(items.__dict__)
 
if __name__ == "__main__":
    app.run()