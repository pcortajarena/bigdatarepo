import json
import numpy as np

with open('PVDAQ_solar_energy_hourly.json', 'r') as fin:
    with open('PVDAQ_solar_energy_hourly_clean.json', 'w') as fout:
        for line in fin:
            obj = json.loads(line)
            for key, value in obj.items():
                if 'data' in value:
                    value['data'] = [dataList for dataList in value['data'] if not np.isnan(dataList[1])]
            json.dump(obj, fout)
