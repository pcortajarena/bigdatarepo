import json
import pandas as pd
from dateparser import parse
from utils import WeatherAPI
from tqdm import tqdm

if __name__ == "__main__":
    with open('data/AUS_wind_energy.json') as f:
        wind_data = json.load(f)

    total = 0
    for k,v in wind_data.items():
        data = v['data']
        total += len(data)

    pbar = tqdm(total=total)
    output = []
    for k,v in wind_data.items():
        lat = v['lat']
        lon = v['lon']
        data = v['data']
        api = WeatherAPI(lat, lon, tp='wind', data_folder='data')
        for d in data:
            item = {}
            time = parse(d[0])
            item['lat'] = lat
            item['lon'] = lon
            item['time'] = time
            item['energy'] = d[1]
            
            weather_data = api.get_weather_data(time)
            
            # Merging python dictionaries
            item = {**item, **weather_data}
            output.append(item)
            pbar.update(1)
    
    df = pd.DataFrame(output)
    df.to_csv('data/wind_energy_with_weather.csv')

