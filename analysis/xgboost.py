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
import importlib
importlib.reload(dlc)
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection  import StratifiedKFold
from scipy.stats import randint, uniform
from dateutil.parser import parse

"""## Model"""

def create_model(**kwargs):
    return xgb.XGBRegressor(**kwargs)

if __name__ == '__main__':  
    TEST_SIZE = 0.20
    GOOGLE_COLAB = False
    SOLAR = True

    dataset = dlc.load_cleaned_data(GOOGLE_COLAB, SOLAR)
    train_all, test = dlc.split_train_test(dataset, test_size=TEST_SIZE)
    train_partial, validation = dlc.split_train_test(train_all, test_size=TEST_SIZE)

    train_partial_x, train_partial_y = dlc.split_x_y(train_partial)
    validation_x, validation_y = dlc.split_x_y(validation)
    
    xg_reg = create_model(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
    
    train_partial_x_values = train_partial_x.values
    train_partial_y_values = train_partial_y.values
    validation_x_values = validation_x.values
    validation_y_values = validation_y.values

    model = dlc.fit_xgboost_model(xg_reg, train_partial_x_values, train_partial_y_values, validation_x_values, validation_y_values, model_name=MODEL_NAME)
    
    preds = model.predict(validation_x_values)
    
    mse = mean_squared_error(validation_y, preds)
    print("MSE: %f" % (mse))
    rmse = np.sqrt(mse)
    print("RMSE: %f" % (rmse))

    """## Hyperparameter tuning experiments"""

    all_x, all_y = dlc.split_x_y(dataset)

    param_distributions = {
        'max_depth': [5],
        'gamma': [0.5, 1],
        'n_estimators': randint(1, 1001),
        'learning_rate': uniform(),
        'subsample': uniform(),
        'colsample_bytree': uniform()
    }
    model = create_model(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                    max_depth = 5, alpha = 10, n_estimators = 2)
    dlc.tune_model_randomized(all_x, all_y, model, param_distributions)

