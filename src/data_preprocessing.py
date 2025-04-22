import numpy as np
import pandas as pd

#prepare features for the model
def prepare_features(df, features, target, X_mean = None, X_std = None):

    #encoding categorical feature
    condition_map = {'Excellent': 3, 'Good': 2, 'regular': 1}
    df['Condition_Encoded'] = df['Condition'].map(condition_map)

    X = df[features].values
    y = df[target].values.reshape(-1, 1)

    #Normalize features an get existing features if any
    if X_mean is None or X_std is None:
        X_mean = np.mean(X, axis=0)
        X_std = np.std(X, axis=0)
        

    X_normalized = (X - X_mean) / X_std

    #add the bias term
    X_final = np.hstack((np.ones((X.shape[0], 1)), X_normalized))

    return X_final, y, X_mean, X_std

#separate training and testing data
def train_test_split(X, y, test_size=0.2):
    indexes = np.random.permutation(X.shape[0])
    test_samples = int(X.shape[0] * test_size)

    X_train = X[indexes[:-test_samples]]
    y_train = y[indexes[:-test_samples]]
    X_test = X[indexes[-test_samples:]]
    y_test = y[indexes[-test_samples:]]

    return X_train, y_train, X_test, y_test