import { WeatherRequest } from './../../model/models';
import { WeatherService } from './../../services/weather.service';
import { EnumsService } from './../../services/enums.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-search-input',
  templateUrl: './search-input.component.html',
  styleUrls: ['./search-input.component.scss']
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
    });
    this.form.controls['isSolar_Ctrl'].valueChanges.subscribe(boolean => {
      this.isSolar = boolean;
    });
  }
  ngOnInit(): void {

  }
  onSubmit(): void {
    const req = new WeatherRequest();
    this.weatherService.getWeather(req).subscribe(weatherResponse => {
      const label = this.isSolar ? 'Solar energy generated' : 'Wind energy generated';
      this.chartDatasets = [
        { data: weatherResponse.data.map(de => de.energy), label },
      ];
      this.chartLabels = weatherResponse.data.map(de => de.date);
    });
  }
}
