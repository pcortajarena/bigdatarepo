from collections import namedtuple

class SolarFarmConfiguration:
    def __init__(self, inverter_mfg, inverter_model, module_mfg, module_model,
                 module_tech, area, azi, elev, power, tilt):
        self.inverter_mfg = inverter_mfg
        self.inverter_model = inverter_model
        self.module_mfg = module_mfg
        self.module_model = module_model
        self.module_tech = module_tech
        self.area = area
        self.azi = azi
        self.elev = elev
        self.power = power
        self.tilt = tilt


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
    def __init__(self, date, energy):
        self.date = date
        self.energy = energy

class WeatherResponse:
    def __init__(self):
        self.data = []
