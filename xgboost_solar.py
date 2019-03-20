# -*- coding: utf-8 -*-
"""BD_xgboost.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11EcQ_YpDpbApFPKmnaHM3h7IqvbqKngR
"""

# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dgBluZYRhUlL0_KF8f7Q5lYFtPXwP489
"""

# -*- coding: utf-8 -*-
"""
## Imports
"""
import pandas as pd
import numpy as np


import xgboost as xgb
from sklearn.metrics import mean_squared_error

import os
import io
import deep_learning_common as dlc
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection  import StratifiedKFold
from scipy.stats import randint, uniform
from dateutil.parser import parse

"""## Load data"""

def load_data():
    GOOGLE_COLAB = True

    if GOOGLE_COLAB:
      # Load the Drive helper and mount
      from google.colab import drive

      # This will prompt for authorization.
      drive.mount('/content/drive', force_remount=True)
      path = os.path.join('drive', 'My Drive', 'data', 'solar_energy_with_weather_2.csv')
    else:
      path = os.path.join('data', 'solar_energy_with_weather_2.csv')
    
    df = pd.read_csv(path)
    return df

"""## Prepare data"""
def clean_data(df):
    encoder = LabelEncoder()
    
    col_to_encode = ["inverter_mfg","inverter_model","module_mfg","module_model","module_tech","inverter_mfg"]
    
    for col in col_to_encode:
      df[col] = encoder.fit_transform(df[col].astype(str))
      
    df['time'] = df.time.apply(lambda time: parse(time))
    df['year'] = df.time.apply(lambda time: time.timetuple().tm_year)
    df['yday'] = df.time.apply(lambda time: time.timetuple().tm_yday)
    df['hour'] = df.time.apply(lambda time: time.timetuple().tm_hour)
    df['sin_hour'] = df.hour.apply(lambda hour: np.sin(np.pi*hour/12))
    df['sin_month'] = df.time.apply(lambda time: np.sin(np.pi*time.timetuple().tm_mon/12))
    
    
    
    df.drop(['Unnamed: 0','time'], axis=1, inplace=True)
    return df

def split_x_y(dataset):
    y_col = 'energy'
  
    train_x = dataset.drop([y_col], axis=1)
    train_y = dataset[[y_col]]
    return train_x, train_y

"""## Model"""

def create_model(**kwargs):
    return xgb.XGBRegressor(**kwargs)

if __name__ == '__main__':  
    TEST_SIZE = 0.20

    dataset = load_data()
    dataset = clean_data(dataset)
    train_all, test = dlc.split_train_test(dataset, test_size=TEST_SIZE)
    train_partial, validation = dlc.split_train_test(train_all, test_size=TEST_SIZE)

    train_partial_x, train_partial_y = split_x_y(train_partial)
    validation_x, validation_y = split_x_y(validation)
    
    xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)

    xg_reg.fit(train_partial_x,train_partial_y)
    
    preds = xg_reg.predict(validation_x)
    
    mse = mean_squared_error(validation_y, preds)
    print("MSE: %f" % (mse))
    rmse = np.sqrt(mse)
    print("RMSE: %f" % (rmse))

"""## Hyperparameter tuning experiments"""

all_x, all_y = split_x_y(dataset)

param_distributions = {
    'max_depth': [5, 10, 15, 20],
    'gamma': [0, 0.5, 1],
    'n_estimators': randint(1, 1001),
    'learning_rate': uniform(),
    'subsample': uniform(),
    'colsample_bytree': uniform()
}
model = create_model(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
dlc.tune_model_randomized(all_x, all_y, model, param_distributions)

