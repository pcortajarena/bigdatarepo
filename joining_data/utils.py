import json
import sys
from glob import glob


class WeatherAPI:

    def __init__(self, lat, lon, tp='solar', data_folder='../data'):
        '''
        It loads the files related to lat and lon in memory to easy and fast access
        '''
        lat = '{:5.3f}'.format(lat)
        lon = '-{:5.3f}'.format(lon)
        parts = [lat, lon]

        # Creating the filename depending on solar or wind data
        filename = '_'.join(parts)
        path = '../{}/{}-weather-jsons-2/{}'.format(data_folder, tp, filename)

        # Getting all files that contain information about the coordinates lat and lon
        paths = glob(path+'*')
        self.weather = {}

        # Load all files for that location in memory (just loaded and read it once)
        for filename in paths:
            splitted_filename = filename.split('_')
            month = splitted_filename[2]
            year = splitted_filename[3]
            with open(filename) as f:
                self.weather[(month, year)] = json.load(f)


    def get_weather_data(self, time):
        '''
        Given the time (datetime python object) it returns the weather attributes for that date
        '''
        output = {}
        month = str(time.month)
        year = str(time.year)
        hour = '0' if time.hour == 0 else str(time.hour)+'00' # The format of the time is: 0, 100, 200, ..., 1400, ..., 2300
        hour_item = None
        day_item = None

        # Getting the weather data we need
        try:
            weather_data = self.weather[(month, year)]['data']['weather']
        except KeyError:
            return None

        # Searching for the date and hour on the selected month and year
        for d in weather_data:
            if d['date'] == time.strftime('%Y-%m-%d'):
                for h in d['hourly']:
                    if h['time'] == hour:
                        day_item = d
                        hour_item = h
                        break

        # Mapping the attributes to the output
        output['sunHour'] = float(day_item['sunHour'])
        output['moon_illumination'] = int(day_item['astronomy'][0]['moon_illumination'])
        output['maxtempC'] = int(day_item['maxtempC'])
        output['mintempC'] = int(day_item['mintempC'])
        output['uvIndex'] = int(day_item['uvIndex'])

        output['tempC'] = int(hour_item['tempC'])
        output['windspeedKmph'] = int(hour_item['windspeedKmph'])
        output['winddirDegree'] = int(hour_item['winddirDegree'])
        output['temperaweatherCodeture'] = int(hour_item['weatherCode'])
        output['precipMM'] = float(hour_item['precipMM'])
        output['humidity'] = int(hour_item['humidity'])
        output['visibility'] = int(hour_item['visibility'])
        output['pressure'] = int(hour_item['pressure'])
        output['cloudcover'] = int(hour_item['cloudcover'])
        output['HeatIndexC'] = int(hour_item['HeatIndexC'])
        output['DewPointC'] = int(hour_item['DewPointC'])
        output['WindChillC'] = int(hour_item['WindChillC'])
        output['WindGustKmph'] = int(hour_item['WindGustKmph'])
        output['FeelsLikeC'] = int(hour_item['FeelsLikeC'])
        
        return output