import { Injectable } from '@angular/core';

import { Http } from '@angular/http';
import { Geolocation } from '@ionic-native/geolocation';
import { UserData } from './user-data';
import { Hotel } from '../objects/hotel';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/observable/of';


@Injectable()
export class HotelData {

  host: string = 'http://178.62.38.12:8108/api';

  constructor(public http: Http, public user: UserData, private geolocation: Geolocation) { }

  load(condition?: any): Observable<Hotel[]> {
    return this.http.get(this.host + '/hotel/filter/1').map(this.processData, this);
  }

  loadNearest(): Observable<Hotel[]> {
    return this.load();
  }

  processData(data: any): Hotel[] {
    // just some good 'ol JS fun with objects and arrays
    // build up the data by linking speakers to sessions
    let hotels = data.json();
    hotels.forEach((hotel: any) => {
      // post process datas
      hotel.rating = parseInt(hotel.rating);
      hotel.priceByHour = hotel.price / hotel.price_unit;
      hotel.nextAvailTimeString = Date.now();
      hotel.propertyType = hotel.room_type;
      hotel.bedroomNumber = hotel.n_beds;
      hotel.guestNumber = hotel.n_guests;
      hotel.bedNumber = hotel.n_rooms;
      hotel.latitude = parseFloat(hotel.location.split(',')[0]);
      hotel.longitude = parseFloat(hotel.location.split(',')[1]);
    });
    return hotels;
  }

}
