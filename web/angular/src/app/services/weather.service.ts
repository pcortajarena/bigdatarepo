import { WeatherRequest, WeatherResponse, DailyEnergy } from './../model/models';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { of } from 'rxjs';
import * as moment from 'moment';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class WeatherService {


  constructor(private http: HttpClient) {
  }

  getWeather(weatherRequest: WeatherRequest): Observable<WeatherResponse> {
    // return this.http.post('http://localhost:4200', JSON.stringify(weatherRequest));
    const resp = new WeatherResponse();
    resp.data = [];

    let mom = moment();

    for (let i = 0; i < 30; i++) {
      mom = mom.subtract(1, 'days');

      const de = new DailyEnergy();
      de.date = mom.format('DD/MM/YYYY');
      de.energy = Math.random() * 10;
      resp.data.push(de);
    }
    return of(resp);
  }
}
