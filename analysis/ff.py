# -*- coding: utf-8 -*-
"""BD_solar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dgBluZYRhUlL0_KF8f7Q5lYFtPXwP489
"""

# -*- coding: utf-8 -*-
"""
## Imports
"""
import pandas as pd

from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

from keras.layers import Dense, LSTM, Embedding
from keras.layers import Conv1D, MaxPooling1D, Flatten, GlobalMaxPooling1D, BatchNormalization
from keras.layers import Concatenate, Subtract, Multiply
from keras.layers import Input, Dropout, PReLU, SpatialDropout1D
from keras.layers import RepeatVector, TimeDistributed


from keras.models import Model, load_model, Sequential

import keras.backend as K

from keras import optimizers

import os
import io
import deep_learning_common as dlc
import importlib
importlib.reload(dlc)
from sklearn.preprocessing import LabelEncoder
from dateutil.parser import parse

"""## Model"""

def create_feed_forward_model(X, Y, kernel_initializer='uniform',activation='relu', optimizer='adam', weight_constraint=0, dense_neurons=100):
    n_features, n_outputs = X.shape[1], Y.shape[1]
    # define model
    input_1 = Input(shape=(n_features,))
    x = Dense(dense_neurons, activation=activation)(input_1)
              
    output = Dense(1, activation='linear')(x)
    
    model = Model(inputs=[input_1], 
                  outputs=output)

    model.compile(loss='mse', optimizer=optimizer)
    return model

"""## Hyperparameter tuning"""
def tune_model(x, y, create_model, n_splits=10):
    # define the grid search parameters
    weight_constraint = [1, 2, 3, 4, 5]
    dense_neurons = [10, 50, 100, 150, 200]
    batch_size = [10, 20, 40, 60, 80, 100]
    epochs = [10, 50, 100]
    
    param_grid = dict(kernel_initializer=dlc.kernel_initializer, activation=dlc.activation, \
                      optimizer=dlc.optimizer, weight_constraint=weight_constraint,  \
                     dense_neurons=dense_neurons, \
                     batch_size=batch_size, epochs=epochs)
    
    dlc.tune_model_grid_keras(x, y, create_model, param_grid, n_splits)

if __name__ == '__main__':  
    TEST_SIZE = 0.20
    EPOCHS = 100
    BATCH_SIZE = 1000
    GOOGLE_COLAB = True
    SOLAR = True
    path = os.path.join(os.path.dirname(__file__), 'models')
    MODEL_NAME = 'ff_solar.h5' if SOLAR else 'ff_wind.h5'
    if not GOOGLE_COLAB:
        MODEL_NAME = os.path.join(path, MODEL_NAME)
    
    dataset = dlc.load_cleaned_data(GOOGLE_COLAB, SOLAR)
    train_all, test = dlc.split_train_test(dataset, test_size=TEST_SIZE)
    train_partial, validation = dlc.split_train_test(train_all, test_size=TEST_SIZE)

    train_partial_x, train_partial_y = dlc.split_x_y(train_partial)
    validation_x, validation_y = dlc.split_x_y(validation)

    model = create_feed_forward_model(train_partial_x, train_partial_y)  
    train_partial_x_values = train_partial_x.values
    train_partial_y_values = train_partial_y.values
    validation_x_values = validation_x.values
    validation_y_values = validation_y.values
    
    model = dlc.fit_keras_model(model, train_partial_x_values, train_partial_y_values, validation_x_values, validation_y_values, model_name=MODEL_NAME, epochs=EPOCHS, batch_size=BATCH_SIZE)
         
    """## Hyperparameter tuning experiments"""
    # RuntimeError: Cannot clone object <keras.wrappers.scikit_learn.KerasClassifier object at 0x7fbeb7fc1128>, as the constructor either does not set or modifies parameter X
    # train_all_x, train_all_y = split_x_y(train_all)
    # 
    # dlc.tune_model_grid_keras(train_all_x, train_all_y, create_feed_forward_model)

