export enum Inverter_mfg_keys {
  SatCon_Technology = 'SatCon Technology',
  SMA = 'SMA',
  Fronius = 'Fronius',
  PV_Powered = 'PV Powered',
  SunPower = 'SunPower',
  Satcon = 'Satcon',
  Solectria = 'Solectria',
  Aurora_PowerOne = 'Aurora PowerOne',
  SMA_America = 'SMA America',
  Trace = 'Trace',
  Enphase = 'Enphase',
  Advanced_Energy = 'Advanced Energy',
  PVPowered = 'PVPowered',
  Xantrex = 'Xantrex',
  ABB = 'ABB',
}

// tslint:disable-next-line:class-name
export interface Inverter_mfg {
  key: Inverter_mfg_keys;
  value: number;
}

export enum Inverter_model_keys {
  IG_7_5 = 'IG+ 7.5',
  _8000f = '8000f',
  _135kW = '135kW',
  IG_4500_LV = 'IG 4500-LV',
  SB4000 = 'SB4000',
  _3_5kW = '3.5kW',
  IG__3_8 = 'IG+ 3.8',
  PVI_13kW = 'PVI 13kW',
  Sunny_Central_250U = 'Sunny Central 250U',
  _75_kVA = '75 kVA',
  Sunny_Boy_3000US = 'Sunny Boy 3000US',
  Power_Gate_Plus_100kW = 'Power Gate Plus 100kW',
  Power_Gate_50kW = 'Power Gate 50kW',
  _50kW = '50kW',
  _30kW = '30kW',
  _250kVA__375kVA = '250kVA, 375kVA',
  _1__100kW___1__50kW = '(1) 100kW, (1) 50kW',
  Power_Gate_Plus_500kW__Power_Gate_Plus_250kW = 'Power Gate Plus 500kW; Power Gate Plus 250kW',
  _4_2kW = '4.2kW',
  _1800 = '1800',
  SB6000 = 'SB6000',
  Power_Gate_Plus_250kW = 'Power Gate Plus 250kW',
  Solaron_333_kVA = 'Solaron 333 kVA',
  Power_Gate_Plus_75kW = 'Power Gate Plus 75kW',
  _3_6kW = '3.6kW',
  _2__PVI_95kW___1__PVI_60kW = '(2) PVI 95kW, (1) PVI 60kW',
  PVS_500_x2___PVS_135_x1_ = 'PVS-500(x2), PVS-135(x1)',
  PVP_30kW = 'PVP 30kW',
  SB5000__SB3000 = 'SB5000 & SB3000',
  D_380 = 'D-380',
  PVI_3000 = 'PVI 3000',
  GT_3_3kW = 'GT 3.3kW',
  _380_5 = '380-5',
  Power_Gate_Plus_135kW = 'Power Gate Plus 135kW',
  _3kW = '3kW',
  __2__SB6000__SB5000 = '(2) SB6000 & SB5000',
  _5_0kW = '5.0kW',
  _4800 = '4800',
  _3500 = '3500',
  PVI_3k = 'PVI 3k',
  IG_3_0_Plus = 'IG 3.0 Plus',
  Solaron_500kW = 'Solaron 500kW',
  PVI_14TL = 'PVI 14TL',
  Tripower_20kW = 'Tripower 20kW',
}

// tslint:disable-next-line:class-name
export interface Inverter_model {
  key: Inverter_model_keys;
  value: number;
}

export enum Module_mfg_keys {
  SunPower = 'SunPower',
  Suntech = 'Suntech',
  Sharp = 'Sharp',
  Canadian_Solar = 'Canadian Solar',
  Schott = 'Schott',
  Sunpower = 'Sunpower',
  Sanyo = 'Sanyo',
  Siemens = 'Siemens',
  Evergreen_Solar = 'Evergreen Solar',
  Mobil = 'Mobil',
  Solar_Cells_Inc = 'Solar Cells, Inc.',
  USSC = 'USSC',
  Silicor_Materials = 'Silicor Materials',
  Shell_Solar = 'Shell Solar',
  UniSolar = 'UniSolar',
  Schuco = 'Schuco',
  Solon = 'Solon',
  Trina_Solar = 'Trina_Solar',
  Evergreen = 'Evergreen',
  Solyndra = 'Solyndra',
  SolarWorld = 'SolarWorld',
  Yingli = 'Yingli',
  Conergy = 'Conergy',
  Suniva = 'Suniva',
}

// tslint:disable-next-line:class-name
export interface Module_mfg {
  key: Module_mfg_keys;
  value: number;
}

export enum Module_model_keys {
  NU_U240F1 = 'NU-U240F1',
  SPR_305_WHT = 'SPR-305-WHT',
  STP_270 = 'STP-270',
  ND_U224C1 = 'ND-U224C1',
  Ra_280_50H = 'Ra 280-50H',
  Poly_230 = 'Poly-230',
  _50W_Prototype_Module = '50W Prototype Module',
  Roof_Shingle = 'Roof Shingle',
  HIP_200_BA3 = 'HIP 200-BA3',
  ES_190 = 'ES-190',
  Eclipse_80 = 'Eclipse 80',
  _240 = '240.0',
  Poly_220 = 'Poly-220',
  SPR_225_BLK = 'SPR-225-BLK',
  STP_175_S__24_Ab_1 = 'STP-175(S)-24/Ab-1',
  STP_200 = 'STP-200',
  CS5P_230 = 'CS5P-230',
  PVL_144 = 'PVL-144',
  SPR_315E_WHT = 'SPR-315E-WHT\r\n',
  M55_c_SI = 'M55 c-SI',
  M55_c_Si = 'M55 c-Si',
  _305_e18_ = '305 (e18)',
  STP_275 = 'STP-275',
  CS6P_200 = 'CS6P-200',
  SPR_315E = 'SPR-315E',
  CS5P_240 = 'CS5P-240',
  Solon_Black_230_01 = 'Solon Black 230/01',
  ES_A_205 = 'ES-A-205',
  SL_001_182 = 'SL-001-182',
  _230_e18_ = '230 (e18)',
  STP_280 = 'STP-280',
  CS6P_230 = 'CS6P-230',
  _260 = '260',
  _318W_x3136_315W_496_ = '318W(x3136), 315W(496)',
  CS6P_235 = 'CS6P-235',
  HIT_220A = 'HIT-220A',
  SPR_320E_WHT_D = 'SPR-320E-WHT-D',
  _225_e18_ = '225 (e18)',
  _238_e19_ = '238 (e19)',
  _185MPE = '185 MPE',
  _315_e19_ = '315 (e19)',
  _320_e19_ = '320 (e19)',
  PM_240P = 'PM-240P',
  Poly225 = 'Poly 225',
  HIT_N220A = 'HIT-N220A',
  ES_180 = 'ES-180',
  PS09_230 = 'PS09-230',
  Poly230 = 'Poly 230',
  HIP_195_BA3 = 'HIP-195-BA3',
  ES_190_ES_195 = 'ES-190, ES-195',
  CS5P_235 = 'CS5P-235',
  HIT_215A = 'HIT-215A',
  OPT270_60_BLK_BLK = 'OPT270-60 BLK-BLK',
  SW_280_Mono = 'SW 280 Mono',
  PM_235P = 'PM-235P',
}

// tslint:disable-next-line:class-name
export interface Module_model {
  key: Module_model_keys;
  value: number;
}

export enum Module_tech_keys {
  Monocrystalline_Silicon = 'Monocrystalline Silicon',
  Polycrystalline_Silicon = 'Polycrystalline Silicon',
  Upgraded_Metallurgical_Grade_Silicon_UMG = 'Upgraded Metallurgical Grade Silicon (UMG)',
  Ribbon_Silicon = 'Ribbon Silicon',
  Amorphous_Silicon_triple_junction = 'Amorphous Silicon (triple junction)',
  Copper_Indium_Gallium_Selenide_CIGS = 'Copper Indium Gallium Selenide (CIGS)',
  Cadmium_Telluride_CdTe = 'Cadmium Telluride (CdTe)',
  Copper_Indium_Selenide_CIS = 'Copper Indium Selenide (CIS)',
}

// tslint:disable-next-line:class-name
export interface Module_tech {
  key: Module_tech_keys;
  value: number;
}

export class SolarFarmConfiguration {
  inverter_mfg: Inverter_mfg;
  inverter_model: Inverter_model;
  module_mfg: Module_mfg;
  module_model: Module_model;
  module_tech: Module_tech;
}

export enum WeatherType {
  SOLAR,
  WIND
}

export class Coordinate {
  lat: number;
  lon: number;
}

export class WeatherRequest {
  farmConfiguration?: SolarFarmConfiguration;
  type: WeatherType;
  month?: number;
  year: number;
  coordinate: Coordinate;
}

export class DailyEnergy {
  date: string;
  energy: number;
}

export class WeatherResponse {
  data: DailyEnergy[];
}
