import { Injectable } from '@angular/core';
import {
  Inverter_mfg,
  Inverter_mfg_keys,
  Inverter_model_keys,
  Inverter_model,
  Module_mfg,
  Module_model,
  Module_mfg_keys,
  Module_model_keys,
  Module_tech,
  Module_tech_keys
} from './../model/models';
@Injectable({
  providedIn: 'root'
})
export class EnumsService {
  Inverter_mfg_list: Inverter_mfg[];
  Inverter_model_list: Inverter_model[];
  Module_mfg_list: Module_mfg[];
  Module_model_list: Module_model[];
  Module_tech_list: Module_tech[];
  constructor() {
    this.Inverter_mfg_list = this.create_key_value_list(Inverter_mfg_keys);
    this.Inverter_model_list = this.create_key_value_list(Inverter_model_keys);
    this.Module_mfg_list = this.create_key_value_list(Module_mfg_keys);
    this.Module_model_list = this.create_key_value_list(Module_model_keys);
    this.Module_tech_list = this.create_key_value_list(Module_tech_keys);
  }
  create_key_value_list(keys_enum): any[] {
    const list = [];
    for (const key in keys_enum) {
      if (key in keys_enum) {
        list.push({ key: keys_enum[key], value: keys_enum[key] });
      }
    }
    return list;
  }
}
