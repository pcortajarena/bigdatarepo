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
    url = '{mainurl}?q={lat:5.3f},{lon:5.3f}&date={startdate}&enddate={enddate}&tp={tp:1d}&format={format}&key={key}'
    url = url.format(mainurl=mainurl,lat=lat, lon=lon, tp=tp, format=f,
                     startdate=startdate, enddate=enddate, key=key)
    print(url)

    # Request the data
    try:
        response = requests.get(url)
        response = json.loads(response.text)
    except:
        pass

    with open('../data/test/{}-{}-{}-{}-{}.json'
                      .format(lat, lon, month, year, counter), 'w') as outfile:
        json.dump(response, outfile)

if __name__ == "__main__":
    with open('../data/PVDAQ_solar_energy_hourly_clean.json') as f:
        solar_data = json.load(f)

    counter = 0
    for k,v in solar_data.items():
        lat = v['site_latitude']
        lon = v['site_longitude']
        if 'data' not in v:
            continue
        data = v['data']
        if data is None or len(data) == 0:
            continue
        start = parse(data[0][0])
        end = parse(data[-1][0])
        month = start.month
        year = start.year
        while year < end.year or (year == end.year and month <= end.month):
            counter += 1
            request_api(lat, lon, month, year, counter)

            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

    print(counter)




