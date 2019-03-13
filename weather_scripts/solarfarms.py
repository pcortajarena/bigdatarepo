import json
import requests
import calendar
from dateparser import parse

def request_api(lat, long, month, year):
    # yyyy-MM-dd
    startdate = '{year:04d}-{month:02d}-01'.format(year=year, month=month)
    enddate = '{year:04d}-{month:02d}-{day:02d}'.format(year=year, month=month, day=calendar.monthrange(year, month)[1])

with open('../data/PVDAQ_solar_energy_hourly_clean.json') as f:
    data = json.load(f)

counter = 0
for k,v in data.items():
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
        request_api(lat, lon, month, year)
        counter += 1
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

print(counter)




