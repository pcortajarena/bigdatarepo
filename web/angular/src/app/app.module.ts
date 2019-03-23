import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import {
  MatButtonModule,
  MatDatepickerModule,
  MatFormFieldModule,
  MatInputModule,
  MatRippleModule,
  MatToolbarModule,
  MatSidenavModule,
  MatIconModule,
  MatListModule,
  MatStepperModule,
  MatCheckboxModule,
  MatRadioModule,
  MatSelectModule,
  MatButtonToggleModule,
  MatSliderModule,
  MatTooltipModule,
  MatSnackBarModule
} from '@angular/material';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatMomentDateModule } from '@angular/material-moment-adapter';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LayoutModule } from '@angular/cdk/layout';
import { HttpClientModule } from '@angular/common/http';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
const modules = [
  MatFormFieldModule,
  MatInputModule,
  MatRippleModule,
  MatDatepickerModule,
  MatMomentDateModule,
  FormsModule,
  ReactiveFormsModule,
  LayoutModule,
  MatToolbarModule,
  MatButtonModule,
  MatSidenavModule,
  MatCheckboxModule,
  MatRadioModule,
  MatSelectModule,
  MatButtonToggleModule,
  MatIconModule,
  MatListModule,
  MatSliderModule,
  MatStepperModule,
  MatPaginatorModule,
  MatCardModule,
  MatTooltipModule,
  MatSnackBarModule,
  MatSlideToggleModule,
  MDBBootstrapModule.forRoot(),
  HttpClientModule,
  BrowserAnimationsModule,
];

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app/app.component';
import { SearchInputComponent } from './components/search-input/search-input.component';
import { MapComponent } from './components/map/map.component';
import { ChartComponent } from './components/chart/chart.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchInputComponent,
    MapComponent,
    ChartComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ...modules,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
