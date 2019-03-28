import os
import pandas as pd
from cleaning import preprocess_solar as p_solar
from cleaning import preprocess_wind as p_wind

def load_data(google_colab = True, solar = True):
    SOLAR_FILE_NAME = 'solar_energy_with_weather.csv'
    WIND_FILE_NAME = 'wind_energy_with_weather.csv'
    SOLAR_FILE_NAME_CLEANED = 'solar_energy_with_weather_cleaned.csv'
    WIND_FILE_NAME_CLEANED = 'wind_energy_with_weather_cleaned.csv'

    FILENAME = SOLAR_FILE_NAME if solar else WIND_FILE_NAME
    FILENAME_CLEANED = SOLAR_FILE_NAME_CLEANED if solar else WIND_FILE_NAME_CLEANED
    CLEANING_LIB = p_solar if solar else p_wind

    if google_colab:
      # Load the Drive helper and mount
      from google.colab import drive

      # This will prompt for authorization.
      drive.mount('/content/drive', force_remount=True)
      DATAPATH = os.path.join('drive', 'My Drive', 'data')
    else:
      DATAPATH = os.path.join('data')
      
    path = os.path.join(DATAPATH, FILENAME)
    cleaned_path = os.path.join(DATAPATH, FILENAME_CLEANED)
    df = pd.read_csv(path, low_memory=False)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    return df, CLEANING_LIB, cleaned_path

if __name__ == '__main__':  
    GOOGLE_COLAB = False

    for boolean in [True, False]:
        df, clean_lib, path = load_data(GOOGLE_COLAB, solar=boolean)
        df = clean_lib.clean_data(df)
        df.to_csv(index=False, path_or_buf=path)
