import json
import requests
import pandas as pd
from tqdm import tqdm
from io import StringIO

# Creates a meta_data_dict that can be called with
# meta_data_dict[system_id], and will provide
# all meta data for that system (solar panel installation)
meta_data_file = 'metadata_pws_pvdaq.csv'
meta_data = pd.read_csv(meta_data_file)
meta_data = meta_data.set_index('system_id')
meta_data_dict = meta_data.to_dict('index')

# Set API parameters that are the same for all calls
format = 'csv'
api_key = '4ak6Xfb7bnFeNig47whAMHBnlPXLz2UgRkM2aeKO'
start_date = '01/01/2000'
end_date = '01/01/2018'
aggregate = 'daily'

# Create API call template
api_standard_call = 'https://developer.nrel.gov/api/pvdaq/v3/' \
                    'site_data.{}' \
                    '?api_key={}' \
                    '&system_id={}' \
                    '&start_date={}' \
                    '&end_date={}' \
                    '&aggregate={}'

# Iterate over every system_id
for system_id in tqdm(meta_data_dict):
    api_call = api_standard_call.format(format, api_key, system_id,
                                        start_date, end_date, aggregate)
    # Read the response into a data frame
    try:
        response = requests.get(api_call)
        response_io = StringIO(response.text)
        respone_df = pd.read_csv(response_io)
    except:
        continue

    # Create a data list: [['2011-09-21',2], ['2011-09-22', 12], ...]
    generated = respone_df['final_yield']
    time = respone_df['measdatetime']
    time_gen = list(zip(time, generated))

    # Save data list to dict
    meta_data_dict[system_id]['data'] = time_gen

# Write dict to file
with open('PVDAQ_solar_energy.json', 'w') as outfile:
    json.dump(meta_data_dict, outfile)
