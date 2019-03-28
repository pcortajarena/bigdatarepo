"""
## Imports
"""
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.metrics import mean_squared_error, mean_absolute_error
from pathlib import Path
import os
import analysis.deep_learning_common as dlc
import importlib
importlib.reload(dlc)


def create_model(**kwargs):
    return svm.SVR(**kwargs)


if __name__ == '__main__':
    TEST_SIZE = 0.20
    GOOGLE_COLAB = False
    SOLAR = True
    cwd = Path().resolve()
    path = os.path.join(os.path.dirname(str(cwd)), 'models')
    MODEL_NAME = 'svm_solar.dat' if SOLAR else 'svm_wind.dat'
    if not GOOGLE_COLAB:
        MODEL_NAME = os.path.join(path, MODEL_NAME)

    dataset = dlc.load_cleaned_data(GOOGLE_COLAB, SOLAR)

    train_all, test = dlc.split_train_test(dataset, test_size=TEST_SIZE)
    train_partial, validation = dlc.split_train_test(train_all,
                                                     test_size=TEST_SIZE)

    train_partial_x, train_partial_y = dlc.split_x_y(train_partial)
    validation_x, validation_y = dlc.split_x_y(validation)

    train_partial_x_values = train_partial_x.values
    train_partial_y_values = train_partial_y.values
    validation_x_values = validation_x.values
    validation_y_values = validation_y.values

    svm_model = create_model(verbose=1)

    model = dlc.fit_svm_model(svm_model, train_partial_x_values,
                                  train_partial_y_values, validation_x_values,
                                  validation_y_values, model_name=MODEL_NAME)

    preds = model.predict(validation_x_values)

    mse = mean_squared_error(validation_y, preds)
    print("MSE: %f" % (mse))
    rmse = np.sqrt(mse)
    print("RMSE: %f" % (rmse))
    mae = mean_absolute_error(validation_y, preds)
    print("MAE: %f" % (mae))
