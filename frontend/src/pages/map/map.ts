import { Component, ViewChild, ElementRef } from '@angular/core';

import { ConferenceData } from '../../providers/conference-data';
import { HotelData } from '../../providers/hotel-data';
import { Geolocation } from '@ionic-native/geolocation';


import { Platform } from 'ionic-angular';


declare var google: any;


@Component({
  selector: 'page-map',
  templateUrl: 'map.html'
})
export class MapPage {

  @ViewChild('mapCanvas') mapElement: ElementRef;
  constructor(public confData: ConferenceData, public platform: Platform, public hotelData: HotelData, private geolocation: Geolocation) {
    this.geolocation.getCurrentPosition().then((resp: any) => {
      // resp.coords.latitude
      // resp.coords.longitude
      console.log(resp);
    }).catch((error: any) => {
      console.log('Error getting location', error);
    });
  }

  ionViewDidLoad() {

    this.hotelData.load().subscribe((data:any) => {
      console.log(data);
    });

    this.confData.getMap().subscribe((mapData: any) => {
      let mapEle = this.mapElement.nativeElement;

      let map = new google.maps.Map(mapEle, {
        center: mapData.find((d: any) => d.center),
        zoom: 16
      });

      mapData.forEach((markerData: any) => {
        let infoWindow = new google.maps.InfoWindow({
          content: `<h5>${markerData.name}</h5>`
        });

        let marker = new google.maps.Marker({
          position: markerData,
          map: map,
          title: markerData.name
        });

        marker.addListener('click', () => {
          infoWindow.open(map, marker);
        });
      });

      google.maps.event.addListenerOnce(map, 'idle', () => {
        mapEle.classList.add('show-map');
      });

    });

  }
}
