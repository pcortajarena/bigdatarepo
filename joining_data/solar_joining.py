import json
import pandas as pd
from dateparser import parse
from utils import WeatherAPI
from tqdm import tqdm

if __name__ == "__main__":
    with open('../data/PVDAQ_solar_energy_hourly_clean.json') as f:
        solar_data = json.load(f)

    total = 0
    for k, v in solar_data.items():
        if 'data' in v.keys():
            data = v['data']
            total += len(data)

    pbar = tqdm(total=total)
    output = []
    for k,v in solar_data.items():
        print(k)
        lat = v['site_latitude']
        lon = v['site_longitude']
        if 'data' in v.keys():
            data = v['data']
            api = WeatherAPI(lat, lon, tp='solar', data_folder='data')

            for d in data:
                item = {}
                time = parse(d[0])
                item['lat'] = lat
                item['lon'] = -lon
                item['elev'] = v.get('site_elevation')
                item['azi'] = v.get('site_azimuth')
                item['tilt'] = v.get('site_tilt')
                item['power'] = v.get('site_power')
                item['area'] = v.get('site_area')
                item['module_mfg'] = v.get('module_mfg')
                item['inverter_mfg'] = v.get('inverter_mfg')
                item['module_model'] = v.get('module_model')
                item['inverter_model'] = v.get('inverter_model')
                item['module_tech'] = v.get('module_tech')
                item['time'] = time
                item['energy'] = d[1]

                weather_data = api.get_weather_data(time)

                # Merging python dictionaries
                if weather_data is not None:
                    item = {**item, **weather_data}
                    output.append(item)
                pbar.update(1)

    df = pd.DataFrame(output)
    df.to_csv('solar_energy_with_weather_2.csv')
