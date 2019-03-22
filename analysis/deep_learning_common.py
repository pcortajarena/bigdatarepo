import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

kernel_initializer = ['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform']
activation = ['softmax', 'softplus', 'softsign', 'relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear']
optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']

"""## Load data"""

def load_cleaned_data(google_colab = True, solar = True):
    SOLAR_FILE_NAME = 'solar_energy_with_weather_2_cleaned.csv'
    WIND_FILE_NAME = 'wind_energy_with_weather_cleaned.csv'
    FILENAME = SOLAR_FILE_NAME if solar else WIND_FILE_NAME

    if google_colab:
      # Load the Drive helper and mount
      from google.colab import drive

      # This will prompt for authorization.
      drive.mount('/content/drive', force_remount=True)
      path = os.path.join('drive', 'My Drive', 'data', FILENAME)
    else:
      path = os.path.join('..','data', FILENAME)
    
    df = pd.read_csv(path)
    return df

"""## Split data"""  

def split_x_y(dataset):
    y_col = 'energy'
  
    train_x = dataset.drop([y_col], axis=1)
    train_y = dataset[[y_col]]
    return train_x, train_y

def split_train_test(dataset, test_size=0.20):
    global RANDOM_STATE
    
    train, test = train_test_split(dataset, test_size=test_size, random_state = RANDOM_STATE)
    return train, test


"""Fit function for a regression model"""
def fit_model(model, train_x_values, train_y_values, val_x_values, val_y_values, epochs=100, batch_size=10, verbose=1, patience=5, model_name='my_model.h5'):
    early_stopping = EarlyStopping(monitor='val_loss', patience=patience)
    model_checkpoint = ModelCheckpoint(model_name, save_best_only=True, save_weights_only=False, monitor='val_loss', mode='min')
    model.fit(train_x_values, train_y_values, \
          validation_data = (val_x_values, val_y_values), \
          batch_size=batch_size, \
          epochs=epochs, \
          verbose=verbose, \
          callbacks=[early_stopping, model_checkpoint]) 
    return model

"""## Hyperparameter tuning"""

def _tune_hyperparameters(grid, x, y):
    grid_result = grid.fit(x.values, y.values)
    # summarize results
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))

"""Hyperparameter optimization with grid search for regression"""
def tune_model_grid_keras(x, y, create_model, param_distributions, n_splits=10, n_iter=10):
    global RANDOM_STATE
    # create model
    model = KerasClassifier(build_fn=create_model, X=x, Y=y)
    
    grid = GridSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=n_splits,
        scoring='neg_mean_squared_error',
        random_state=RANDOM_STATE,
        n_jobs=-1 # in parallel
    ) 
    _tune_hyperparameters(grid, x, y)


def tune_model_randomized_keras(x, y, create_model, param_distributions, n_splits=10, n_iter=10):
    global RANDOM_STATE
    # create model
    model = KerasClassifier(build_fn=create_model, X=x, Y=y)
    
    grid = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=n_splits,
        scoring='neg_mean_squared_error',
        random_state=RANDOM_STATE,
        n_jobs=-1 # in parallel
    ) 
    _tune_hyperparameters(grid, x, y)

def tune_model_grid(x, y, model, param_distributions, n_splits=10, n_iter=10):
    global RANDOM_STATE
    # create model
    grid = GridSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=n_splits,
        scoring='neg_mean_squared_error',
        random_state=RANDOM_STATE,
        n_jobs=-1 # in parallel
    ) 
    _tune_hyperparameters(grid, x, y)

def tune_model_randomized(x, y, model, param_distributions, n_splits=10, n_iter=10):
    global RANDOM_STATE
    # create model
    grid = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=n_splits,
        scoring='neg_mean_squared_error',
        random_state=RANDOM_STATE,
        n_jobs=-1 # in parallel
    ) 
    _tune_hyperparameters(grid, x, y)

