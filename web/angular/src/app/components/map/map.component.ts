import { Coordinate } from './../../model/models';
import { Component, OnInit, forwardRef, Input } from '@angular/core';
import { icon, Marker } from 'leaflet';
import { ControlValueAccessor, NG_VALUE_ACCESSOR } from '@angular/forms';
declare let L;
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss'],
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => MapComponent),
      multi: true
    }
  ]
})
export class MapComponent implements OnInit, ControlValueAccessor {
  map: any;
  marker: any;

  // tslint:disable-next-line:no-input-rename
  @Input('coordinate') _coordinate: Coordinate;

  get coordinate() {
    return this._coordinate;
  }

  set coordinate(val) {
    this._coordinate = val;
    this.propagateChange(val);
  }
  propagateChange = (_: any) => { };
  constructor() { }

  ngOnInit(): void {
    this.map = L.map('map').setView([51.505, -0.09], 13);
    this.fixIssueIcons();
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {}).addTo(this.map);
    this.map.on('click', e => this.onMapClick(e));
  }
  writeValue(value: any): void {
    if (value) {
      this.coordinate = value;
    }
  }
  registerOnChange(fn: any): void {
    this.propagateChange = fn;
  }
  registerOnTouched(fn: any): void {
  }
  private onMapClick(e) {
    this.addMarker(e.latlng);
  }
  private addMarker({ lat, lng }: { lat: number, lng: number }): void {
    if (this.marker) {
      this.map.removeLayer(this.marker);
    }
    this.marker = new L.Marker({ lat, lng }).addTo(this.map);
    const coord = new Coordinate();
    coord.lat = lat;
    coord.lon = lng;
    this.coordinate = coord;
    this.propagateChange(coord);
  }
  private fixIssueIcons() {
    const iconRetinaUrl = 'assets/marker-icon-2x.png';
    const iconUrl = 'assets/marker-icon.png';
    const shadowUrl = 'assets/marker-shadow.png';
    const iconDefault = icon({
      iconRetinaUrl,
      iconUrl,
      shadowUrl,
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      tooltipAnchor: [16, -28],
      shadowSize: [41, 41]
    });
    Marker.prototype.options.icon = iconDefault;
  }
}
