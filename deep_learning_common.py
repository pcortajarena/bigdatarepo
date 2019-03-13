import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

kernel_initializer = ['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform']
activation = ['softmax', 'softplus', 'softsign', 'relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear']
optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']

def split_train_test(dataset, test_size=0.20):
    global RANDOM_STATE
    
    train, test = train_test_split(dataset, test_size=test_size, random_state = RANDOM_STATE)
    return train, test


"""Fit function for a regression model"""
def fit_model(model, train_x_values, train_y_values, val_x_values, val_y_values, epochs=100, batch_size=10, verbose=1, patience=5, model_name='my_model.h5'):
    early_stopping = EarlyStopping(monitor='val_mse', patience=patience)
    model_checkpoint = ModelCheckpoint(model_name, save_best_only=True, save_weights_only=False, monitor='val_loss', mode='min')
    model.fit(train_x_values, train_y_values, \
          validation_data = (val_x_values, val_y_values), \
          batch_size=batch_size, \
          epochs=epochs, \
          verbose=verbose, \
          callbacks=[early_stopping, model_checkpoint]) 
    return model

"""## Hyperparameter tuning"""

"""Hyperparameter optimization with grid search for regression"""
def tune_model(x, y, create_model, param_grid, n_splits=10):
    global RANDOM_STATE
    # create model
    model = KerasClassifier(build_fn=create_model, X=x, Y=y)
    
    cv = StratifiedKFold(n_splits, shuffle=True, random_state=RANDOM_STATE)
    
    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=cv,
        scoring='neg_mean_squared_error',
        n_jobs=-1 # in parallel
    ) 
    grid_result = grid.fit(x.values, y.values)
    # summarize results
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))
