import json
import pandas as pd
from utils import WeatherAPI

if __name__ == "__main__":
    with open('../data/PVDAQ_solar_energy_hourly_clean.json') as f:
        solar_data = json.load(f)

    output = []
    for k,v in solar_data.items():
        # TODO
        # api = WeatherAPI(lat, lon)
        # Then, you can call: api.get_weather_data(time)
        # where time is a datetime object with date and hour
        # You can take a look to wind_joining.py
        pass
    
    df = pd.DataFrame(output)
    df.to_csv('data/solar_energy_with_weather.csv')

