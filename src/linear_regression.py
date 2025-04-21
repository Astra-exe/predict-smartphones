import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.theta = None #Model weights
        self.loss_history = []
    
    def fit(self, X, y):
        #train the model with gradient descent
        m,n = X.shape
        self.theta = np.zeros((n,1))

        for epoch in range(self.epochs):
            #predictions and error
            y_pred = X.dot(self.theta)
            error = y_pred - y

            #cost (MSE)
            cost = (1/(2*m)) * np.sum(error**2)
            self.loss_history.append(cost)

            #calculate gradients
            gradients = (1/m) * X.T.dot(error)

            #update weights
            self.theta -= self.lr * gradients
        return self
    
    def predict(self, X):
        #make predictions
        return X.dot(self.theta)
    
    #Functions for metrics
    def mse(self, y_true, y_pred):
        #calculate the mean square error
        return np.mean((y_true-y_pred)**2)
    
    def r2_score(self, y_true, y_pred):
        #calculate the r^2 score
        ss_total = np.sum((y_true - np.mean(y_true))**2)
        ss_res = np.sum((y_true-y_pred)**2)
        return 1 - (ss_res/ss_total)