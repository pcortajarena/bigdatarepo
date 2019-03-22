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


"""## Load data"""

def load_data():
    path = os.path.join('data', 'dummy_data.csv')
    data = pd.read_csv(path)
    return data

"""## Prepare data"""

def split_x_y(dataset):
    train_x = dataset.drop(['y'], axis=1)
    train_y = dataset[['y']]
    return train_x, train_y
  
def reshape_3d(dataset, n_timesteps=1):
    return dataset.values.reshape((dataset.shape[0], n_timesteps, dataset.shape[1]))

"""## Model"""

def create_lstm_model(X, Y, kernel_initializer='uniform',activation='relu', optimizer='adam', weight_constraint=0, lstm_neurons=200, dense_neurons=100, n_timesteps=1):
    n_features, n_outputs = X.shape[1], Y.shape[1]
    # define model
    model = Sequential()
    model.add(LSTM(lstm_neurons, activation=activation, input_shape=(n_timesteps, n_features)))
    model.add(RepeatVector(n_outputs))
    model.add(LSTM(lstm_neurons, activation=activation, return_sequences=True))
    model.add(TimeDistributed(Dense(dense_neurons, activation=activation, kernel_initializer=kernel_initializer)))
    model.add(TimeDistributed(Dense(1)))
    model.compile(loss='mse', optimizer=optimizer)
    return model

"""## Hyperparameter tuning"""
def tune_model(x, y, create_model, n_splits=10):
    # define the grid search parameters
    weight_constraint = [1, 2, 3, 4, 5]
    lstm_neurons = [10, 50, 100, 150, 200]
    dense_neurons = [10, 50, 100, 150, 200]
    batch_size = [10, 20, 40, 60, 80, 100]
    epochs = [10, 50, 100]
    
    
    param_grid = dict(kernel_initializer=dlc.kernel_initializer, activation=dlc.activation, \
                      optimizer=dlc.optimizer, weight_constraint=weight_constraint,  \
                     lstm_neurons=lstm_neurons, dense_neurons=dense_neurons, \
                     batch_size=batch_size, epochs=epochs)
    
    dlc.tune_model(x, y, create_model, param_grid, n_splits)

"""## Experiments"""
if __name__ == '__main__':  
    TEST_SIZE = 0.20
    N_TIMESTEPS = 1
    EPOCHS = 10000

    dataset = load_data()
    train_all, test = dlc.split_train_test(dataset, test_size=TEST_SIZE)
    train_partial, validation = dlc.split_train_test(train_all, test_size=TEST_SIZE)

    train_partial_x, train_partial_y = split_x_y(train_partial)
    validation_x, validation_y = split_x_y(validation)

    model = create_lstm_model(train_partial_x, train_partial_y, n_timesteps=N_TIMESTEPS)

    train_partial_x_values = reshape_3d(train_partial_x, n_timesteps=N_TIMESTEPS)
    train_partial_y_values = reshape_3d(train_partial_y, n_timesteps=N_TIMESTEPS)
    validation_x_values = reshape_3d(validation_x, n_timesteps=N_TIMESTEPS)
    validation_y_values = reshape_3d(validation_y, n_timesteps=N_TIMESTEPS)


    model = dlc.fit_model(model, train_partial_x_values, train_partial_y_values, validation_x_values, validation_y_values, model_name='ml_lstm_1.h5', epochs=EPOCHS)

"""## Hyperparameter tuning experiments"""

    # RuntimeError: Cannot clone object <keras.wrappers.scikit_learn.KerasClassifier object at 0x7fbeb7fc1128>, as the constructor either does not set or modifies parameter X
    # train_all_x, train_all_y = split_x_y(train_all)
    # 
    # dlc.tune_model(train_all_x, train_all_y, create_lstm_model)

