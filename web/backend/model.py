class SolarFarmConfiguration:
    def __init__(self, inverter_mfg, inverter_model, module_mfg, module_model, module_tech):
        self.inverter_mfg = inverter_mfg
        self.inverter_model = inverter_model
        self.module_mfg = module_mfg
        self.module_model = module_model
        self.module_tech = module_tech

class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class WeatherRequest:
    def __init__(self, farmConfiguration, solar, startMonthYear, endMonthYear, coordinate):
        self.farmConfiguration = SolarFarmConfiguration(**farmConfiguration)
        self.solar = solar
        self.startMonthYear = startMonthYear
        self.endMonthYear = endMonthYear
        self.coordinate = Coordinate(**coordinate)

class DailyEnergy:
    date = ""
    energy = int()

class WeatherResponse:
    data = [DailyEnergy()]
