import { Injectable } from '@angular/core';

import { Http } from '@angular/http';

import { UserData } from './user-data';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/observable/of';


@Injectable()
export class HotelData {

  host: string = 'http://178.62.38.12/api';

  constructor(public http: Http, public user: UserData) { }

  load(condition: any): any {
    return this.http.get(this.host + '/hotel/filter/1').map(this.processData, this);
  }

  loadNearest(location: any) {
    return this.load({});
  }

  processData(data: any) {
    // just some good 'ol JS fun with objects and arrays
    // build up the data by linking speakers to sessions
    let hotels = data.json();
    hotels.forEach((hotel: any) => {
      // post process datas
      hotel.rating = parseInt(hotel.rating);
      hotel.price = parseInt(hotel.price);

    });
    return hotels;
  }

}
