import json
import numpy as np

path_in = os.path.join("data", "PVDAQ_solar_energy_hourly.json")
path_out = os.path.join("data", "PVDAQ_solar_energy_hourly_clean.json")

with open(path_in, 'r') as fin:
    with open(path_out, 'w') as fout:
        for line in fin:
            obj = json.loads(line)
            for key, value in obj.items():
                if 'data' in value:
                    value['data'] = [dataList for dataList in value['data'] if not np.isnan(dataList[1])]
            json.dump(obj, fout)
