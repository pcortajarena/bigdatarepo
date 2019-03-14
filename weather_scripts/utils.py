import calendar
import json
import requests

API_KEYS=[
    #'0fc0f26c3b264533aeb135149191303',
    #'76cfa3225e0945ceb2d135337191303',
    #'e82e4fd8ba5140a3b99135432191303',
    #'5d63814a8cf043a9912135534191303',
    #'0f3b36273439481cb42135704191303',
    #'784747442a2a475ba7e135813191303',
    #'534b86c931a94e5ebb8140033191303',
    #'6a499521111e45ccab0135500191303',
    #'963aba864e25442191f135732191303',
    #'880ee119290b455b95d135842191303',
    'be844d8013584670885135959191303',
    '363c7bcccda14b3caf4135912191303'
    ]

def request_api(lat, lon, month, year, counter, outfolder, debug=True):

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

    # Request the data
    if debug:
        print(url)
    else:
        try:
            response = requests.get(url)
            response = json.loads(response.text)
        except Exception as e: 
            print(e)

        with open('../data/{}/{}_{}_{}_{}_{}.json'
                        .format(outfolder,lat, lon, month, year, counter), 'w') as outfile:
            json.dump(response, outfile)