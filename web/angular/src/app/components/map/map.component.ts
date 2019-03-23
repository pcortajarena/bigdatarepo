import { Component, OnInit } from '@angular/core';
import { icon, Marker } from 'leaflet';
declare let L;
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  map: any;
  marker: any;
  constructor() { }

  ngOnInit(): void {
    this.map = L.map('map').setView([51.505, -0.09], 13);
    this.fixIssueIcons();
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {}).addTo(this.map);
    this.map.on('click', e => this.onMapClick(e));
  }
  private onMapClick(e) {
    this.addMarker(e.latlng);
    // send coordinate up
  }
  private addMarker({ lat, lng }: { lat: number, lng: number }): void {
    if (this.marker) {
      this.map.removeLayer(this.marker);
    }
    this.marker = new L.Marker({ lat, lng }).addTo(this.map);
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
