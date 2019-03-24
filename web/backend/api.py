from random import choice
import calendar
import json
import requests

class WeatherAPI:

    API_KEYS=[
        '0fc0f26c3b264533aeb135149191303',
        '76cfa3225e0945ceb2d135337191303',
        'e82e4fd8ba5140a3b99135432191303',
        '5d63814a8cf043a9912135534191303',
        '0f3b36273439481cb42135704191303',
        '784747442a2a475ba7e135813191303',
        '534b86c931a94e5ebb8140033191303',
        '6a499521111e45ccab0135500191303',
        '963aba864e25442191f135732191303',
        '880ee119290b455b95d135842191303',
        'be844d8013584670885135959191303',
        '363c7bcccda14b3caf4135912191303'
    ]

    def __init__(self, lat, lon):
        self.lat = '{:5.3f}'.format(lat)
        self.lon = '{:5.3f}'.format(lon)
        self.weather = {}

    def _call_api(self, month, year):
        # yyyy-MM-dd
        mainurl = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx'
        tp = 1
        f = 'json'
        startdate = '{year:04d}-{month:02d}-01'.format(year=year, month=month)
        enddate = '{year:04d}-{month:02d}-{day:02d}'\
            .format(year=year, month=month, day=calendar.monthrange(year, month)[1])
        key = choice(self.API_KEYS)
        url = '{mainurl}?q={lat},{lon}&date={startdate}&enddate={enddate}&tp={tp:1d}&format={format}&key={key}'
        url = url.format(mainurl=mainurl,lat=self.lat, lon=self.lon, tp=tp, format=f,
                        startdate=startdate, enddate=enddate, key=key)

        # Request the data
        try:
            response = requests.get(url)
            response = json.loads(response.text)
            return response
        except Exception as e: 
            print(e)

    def get_weather_data(self, time):
        '''
        Given the time (datetime python object) it returns the weather attributes for that date
        '''
        output = {}
        month = time.month
        year = time.year
        hour = '0' if time.hour == 0 else str(time.hour)+'00' # The format of the time is: 0, 100, 200, ..., 1400, ..., 2300
        hour_item = None
        day_item = None

        # Getting the weather data we need
        if (month, year) not in self.weather:
            # Get data
            self.weather[(month, year)] = self._call_api(month, year)
        weather_data = self.weather[(month, year)]['data']['weather']

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