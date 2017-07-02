import { Slides } from 'ionic-angular';
import { Component, ViewChild} from '@angular/core';
import { Hotel } from '../../objects/hotel'

@Component({
  selector: 'hotel-detail',
  templateUrl: 'hotel-detail.html'
})


export class HotelDetailPage {
  @ViewChild('thisHotel') thisHotel: Hotel;

  constructor(
    public hotel: Hotel,
  ){}

}
