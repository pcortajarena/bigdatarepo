import { WeatherRequest, WeatherResponse, DailyEnergy } from './../model/models';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { of } from 'rxjs';
import { map } from 'rxjs/operators';
import * as moment from 'moment';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class WeatherService {


  constructor(private http: HttpClient) {
  }

  getWeather(weatherRequest: WeatherRequest): Observable<WeatherResponse> {
    const response = {
      "data": [
        {
          "date": "2018-12-01T00:00:00",
          "energy": 15.383469581604004
        },
        {
          "date": "2018-12-02T00:00:00",
          "energy": 14.795157432556152
        },
        {
          "date": "2018-12-03T00:00:00",
          "energy": 15.249120712280273
        },
        {
          "date": "2018-12-04T00:00:00",
          "energy": 16.17962646484375
        },
        {
          "date": "2018-12-05T00:00:00",
          "energy": 15.287920951843262
        },
        {
          "date": "2018-12-06T00:00:00",
          "energy": 14.736732482910156
        },
        {
          "date": "2018-12-07T00:00:00",
          "energy": 15.139522552490234
        },
        {
          "date": "2018-12-08T00:00:00",
          "energy": 15.91498851776123
        },
        {
          "date": "2018-12-09T00:00:00",
          "energy": 15.729928970336914
        },
        {
          "date": "2018-12-10T00:00:00",
          "energy": 16.24418067932129
        },
        {
          "date": "2018-12-11T00:00:00",
          "energy": 16.100902557373047
        },
        {
          "date": "2018-12-12T00:00:00",
          "energy": 15.843002319335938
        },
        {
          "date": "2018-12-13T00:00:00",
          "energy": 15.964593887329102
        },
        {
          "date": "2018-12-14T00:00:00",
          "energy": 15.95129108428955
        },
        {
          "date": "2018-12-15T00:00:00",
          "energy": 16.804323196411133
        },
        {
          "date": "2018-12-16T00:00:00",
          "energy": 15.220990180969238
        },
        {
          "date": "2018-12-17T00:00:00",
          "energy": 15.529613494873047
        },
        {
          "date": "2018-12-18T00:00:00",
          "energy": 15.710284233093262
        },
        {
          "date": "2018-12-19T00:00:00",
          "energy": 15.320198059082031
        },
        {
          "date": "2018-12-20T00:00:00",
          "energy": 15.16258430480957
        },
        {
          "date": "2018-12-21T00:00:00",
          "energy": 15.183223724365234
        },
        {
          "date": "2018-12-22T00:00:00",
          "energy": 15.278532981872559
        },
        {
          "date": "2018-12-23T00:00:00",
          "energy": 15.07595157623291
        },
        {
          "date": "2018-12-24T00:00:00",
          "energy": 15.876708030700684
        },
        {
          "date": "2018-12-25T00:00:00",
          "energy": 15.621695518493652
        },
        {
          "date": "2018-12-26T00:00:00",
          "energy": 15.272908210754395
        },
        {
          "date": "2018-12-27T00:00:00",
          "energy": 15.899044036865234
        },
        {
          "date": "2018-12-28T00:00:00",
          "energy": 15.21950912475586
        },
        {
          "date": "2018-12-29T00:00:00",
          "energy": 15.100261688232422
        },
        {
          "date": "2018-12-30T00:00:00",
          "energy": 15.159747123718262
        },
        {
          "date": "2018-12-31T00:00:00",
          "energy": 14.436483383178711
        }
      ]
    };
    return this.http.post('http://localhost:5000', JSON.stringify(weatherRequest), {
      headers: {
        'Content-Type': 'application/json',
      }
    }).pipe(map(r => <WeatherResponse>r));
    // const resp = new WeatherResponse();
    // resp.data = [];
    // let mom = moment();
    // for (let i = 0; i < 30; i++) {
    //   mom = mom.subtract(1, 'days');
    //   const de = new DailyEnergy();
    //   de.date = mom.format('DD/MM/YYYY');
    //   de.energy = Math.random() * 10;
    //   resp.data.push(de);
    // }
    // return of(resp);
  }
}
