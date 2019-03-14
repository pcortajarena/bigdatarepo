import json
import requests
import calendar
from dateparser import parse
import os

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
    '880ee119290b455b95d135842191303'
    ]

API_KEYS_COUNTER = 0

def request_api(lat, lon, month, year, counter):

    # yyyy-MM-dd
    mainurl = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx'
    tp = 1
    f = 'json'
    startdate = '{year:04d}-{month:02d}-01'.format(year=year, month=month)
    enddate = '{year:04d}-{month:02d}-{day:02d}'\
        .format(year=year, month=month, day=calendar.monthrange(year, month)[1])
    key = API_KEYS[counter//490]
    url = '{mainurl}?q={lat},{lon}&date={startdate}&enddate={enddate}&tp={tp:1d}&format={format}&key={key}'
    url = url.format(mainurl=mainurl,lat=lat, lon=lon, tp=tp, format=f,
                     startdate=startdate, enddate=enddate, key=key)
    print(url)

    # Request the data
    try:
        response = requests.get(url)
        response = json.loads(response.text)
    except Exception as e: 
        print(e)

    with open('../data/solar-weather-jsons/{}-{}-{}-{}-{}.json'
                      .format(lat, lon, month, year, counter), 'w') as outfile:
        json.dump(response, outfile)

if __name__ == "__main__":
    with open('../data/PVDAQ_solar_energy_hourly_clean.json') as f:
        solar_data = json.load(f)

    counter = 0
    farms = dict()
    for k,v in solar_data.items():
        lat = '{:5.3f}'.format(v['site_latitude'])
        lon = '{:5.3f}'.format(v['site_longitude'])
        if 'data' not in v:
            continue
        data = v['data']
        if data is None or len(data) == 0:
            continue
        
        startdate = parse(data[0][0])
        enddate = parse(data[-1][0])
        if (lat, lon) not in farms:
            farms[(lat, lon)] = dict()
            farms[(lat, lon)]['startdate'] = startdate
            farms[(lat, lon)]['enddate'] = enddate
            continue
        
        if startdate < farms[(lat, lon)]['startdate']:
            farms[(lat, lon)]['startdate'] = startdate
        
        if enddate > farms[(lat, lon)]['enddate']:
            farms[(lat, lon)]['enddate'] = enddate

    for (lat,lon),v in farms.items():
        month = v['startdate'].month
        year = v['startdate'].year
        while year < v['enddate'].year or (year == v['enddate'].year and month <= v['enddate'].month):
            counter += 1
            request_api(lat, lon, month, year, counter)

            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

    print(counter)




