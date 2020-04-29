import json
from dateparser import parse
import os
from utils import request_api

if __name__ == "__main__":
    with open('../data/AUS_wind_energy.json') as f:
        wind_data = json.load(f)

    counter = 0
    farms = dict()
    for k,v in wind_data.items():
        lat = '{:5.3f}'.format(v['lat'])
        lon = '{:5.3f}'.format(v['lon'])
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
            request_api(lat, lon, month, year, counter, 'wind-weather-jsons', debug=True)

            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

    print(counter)




