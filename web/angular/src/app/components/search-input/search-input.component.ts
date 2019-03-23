import { WeatherRequest, SolarFarmConfiguration } from './../../model/models';
import { WeatherService } from './../../services/weather.service';
import { EnumsService } from './../../services/enums.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MomentDateAdapter } from '@angular/material-moment-adapter';
import { DateAdapter, MAT_DATE_FORMATS, MAT_DATE_LOCALE } from '@angular/material/core';
import { MatDatepicker } from '@angular/material/datepicker';

// Depending on whether rollup is used, moment needs to be imported differently.
// Since Moment.js doesn't have a default export, we normally need to import using the `* as`
// syntax. However, rollup creates a synthetic default module and we thus need to import it using
// the `default as` syntax.
import * as moment from 'moment';
// tslint:disable-next-line:no-duplicate-imports
import { Moment } from 'moment';


// See the Moment.js docs for the meaning of these formats:
// https://momentjs.com/docs/#/displaying/format/
export const MY_FORMATS = {
  parse: {
    dateInput: 'MM/YYYY',
  },
  display: {
    dateInput: 'MM/YYYY',
    monthYearLabel: 'MMM YYYY',
    dateA11yLabel: 'LL',
    monthYearA11yLabel: 'MMMM YYYY',
  },
};

@Component({
  selector: 'app-search-input',
  templateUrl: './search-input.component.html',
  styleUrls: ['./search-input.component.scss'],
  providers: [
    // `MomentDateAdapter` can be automatically provided by importing `MomentDateModule` in your
    // application's root module. We provide it at the component level here, due to limitations of
    // our example generation script.
    { provide: DateAdapter, useClass: MomentDateAdapter, deps: [MAT_DATE_LOCALE] },

    { provide: MAT_DATE_FORMATS, useValue: MY_FORMATS },
  ],
})
export class SearchInputComponent implements OnInit {
  form: FormGroup;
  isSolar: boolean;
  chartDatasets: Array<any> = [];
  chartLabels: Array<any> = [];

  Inverter_mfg_list = this.enumsService.Inverter_mfg_list;
  Inverter_model_list = this.enumsService.Inverter_model_list;
  Module_mfg_list = this.enumsService.Module_mfg_list;
  Module_model_list = this.enumsService.Module_model_list;
  Module_tech_list = this.enumsService.Module_tech_list;


  constructor(private enumsService: EnumsService,
    private _fb: FormBuilder,
    private weatherService: WeatherService) {
    this.isSolar = true;
    this.form = this._fb.group({
      isSolar_Ctrl: [true],
      inverter_mfg_Ctrl: [null, Validators.required],
      inverter_model_Ctrl: [null, Validators.required],
      module_mfg_Ctrl: [null, Validators.required],
      module_model_Ctrl: [null, Validators.required],
      module_tech_Ctrl: [null, Validators.required],
      coordinateCtrl: [null, Validators.required],
      startDateCtrl: [moment(), Validators.required],
      endDateCtrl: [moment(), Validators.required],
    });
    this.form.controls['isSolar_Ctrl'].valueChanges.subscribe(boolean => {
      this.isSolar = boolean;
      const required = Validators.required;
      if (this.isSolar) {
        this.form.controls['inverter_mfg_Ctrl'].setValidators(required);
        this.form.controls['inverter_model_Ctrl'].setValidators(required);
        this.form.controls['module_mfg_Ctrl'].setValidators(required);
        this.form.controls['module_model_Ctrl'].setValidators(required);
        this.form.controls['module_tech_Ctrl'].setValidators(required);
      } else {
        this.form.controls['inverter_mfg_Ctrl'].clearValidators();
        this.form.controls['inverter_model_Ctrl'].clearValidators();
        this.form.controls['module_mfg_Ctrl'].clearValidators();
        this.form.controls['module_model_Ctrl'].clearValidators();
        this.form.controls['module_tech_Ctrl'].clearValidators();
      }

      this.form.controls['inverter_mfg_Ctrl'].updateValueAndValidity();
      this.form.controls['inverter_model_Ctrl'].updateValueAndValidity();
      this.form.controls['module_mfg_Ctrl'].updateValueAndValidity();
      this.form.controls['module_model_Ctrl'].updateValueAndValidity();
      this.form.controls['module_tech_Ctrl'].updateValueAndValidity();
    });
  }
  ngOnInit(): void {

  }
  onSubmit(): void {
    const {
      isSolar_Ctrl,
      inverter_mfg_Ctrl,
      inverter_model_Ctrl,
      module_mfg_Ctrl,
      module_model_Ctrl,
      module_tech_Ctrl,
      coordinateCtrl,
      startDateCtrl,
      endDateCtrl,
    } = this.form.getRawValue();
    const req = new WeatherRequest();
    if (isSolar_Ctrl) {
      const solarFarmConfiguration = new SolarFarmConfiguration();
      solarFarmConfiguration.inverter_mfg = inverter_mfg_Ctrl;
      solarFarmConfiguration.inverter_model = inverter_model_Ctrl;
      solarFarmConfiguration.module_mfg = module_mfg_Ctrl;
      solarFarmConfiguration.module_model = module_model_Ctrl;
      solarFarmConfiguration.module_tech = module_tech_Ctrl;
      req.farmConfiguration = solarFarmConfiguration;
    }
    req.solar = isSolar_Ctrl;
    req.coordinate = coordinateCtrl;
    req.startMonthYear = startDateCtrl.format('MM/YYYY');
    req.endMonthYear = endDateCtrl.format('MM/YYYY');
    this.weatherService.getWeather(req).subscribe(weatherResponse => {
      const label = this.isSolar ? 'Solar energy generated' : 'Wind energy generated';
      this.chartDatasets = [
        { data: weatherResponse.data.map(de => de.energy), label },
      ];
      this.chartLabels = weatherResponse.data.map(de => de.date);
    });
  }
  chosenYearHandler(normalizedYear: Moment, controlName: string) {
    const ctrlValue = this.form.controls[controlName].value;
    ctrlValue.year(normalizedYear.year());
    this.form.controls[controlName].setValue(ctrlValue);
  }

  chosenMonthHandler(normalizedMonth: Moment, datepicker: MatDatepicker<Moment>, controlName: string) {
    const ctrlValue = this.form.controls[controlName].value;
    ctrlValue.month(normalizedMonth.month());
    this.form.controls[controlName].setValue(ctrlValue);
    datepicker.close();
  }
}
