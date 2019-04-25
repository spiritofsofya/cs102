import pandas as pd
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler


class GDRegressor:

    def __init__(self, alpha=0.01, n_iter=100):
        self.alpha = alpha
        self.n_iter = n_iter

    def fit(self, x_train, y_train):  # x - матрица признаков, y - вектор ответов
        if type(x_train) == list:
            pass
        else:
            x_train = x_train.values.tolist()

        if type(y_train) == list:
            pass
        else:
            y_train = y_train.values.tolist()

        x_matrix = []
        for i in range(len(x_train)):
            x_train[i].insert(0, 1)
            x_matrix.append(x_train[i])
        x_as_matrix = np.asmatrix(x_matrix)

        y_matrix = []
        for i in range(len(y_train)):
            y_matrix.append([y_train[i]])

        m = len(y_train)
        self.theta = np.zeros((len(x_matrix[0]), 1))

        for i in range(self.n_iter):
            self.theta = self.theta - self.alpha * (1 / m) * (np.matmul(x_as_matrix.T,
                                                                        (np.matmul(x_matrix, self.theta) - y_matrix)))

        theta_list = np.matrix.tolist(self.theta)

        self.coef_ = theta_list[1:]  # coef - параметры тетта(i)
        self.intercept_ = theta_list[0]  # coef - параметр тетта(0)

        return theta_list

    def predict(self, x_test):
        if type(x_test) == list:
            pass
        else:
            x_test = x_test.values.tolist()
        x_matrix_test = []
        for i in range(len(x_test)):
            x_test[i].insert(0, 1)
            x_matrix_test.append(x_test[i])
        answers = np.matmul(x_matrix_test, self.theta)
        return answers


def rmse(y_hat, y):
    """ Root mean squared error """
    if type(y) == list:
        pass
    else:
        y = y.values.tolist()
    m = len(y)
    sum = 0
    for i in range(m):
        sum += ((y_hat[i] - y[i]) ** 2 / m)
    error = np.sqrt(sum)
    return error


def r_squared(y_hat, y):
    """ R-squared score """
    if type(y) == list:
        pass
    else:
        y = y.values.tolist()
    m = len(y)
    y_avg = np.average(y)

    a = b = 0
    for i in range(m):
        a += (y[i] - y_hat[i]) ** 2
        b += (y[i] - y_avg) ** 2
    error = 1 - a / b
    return error


if __name__ == '__main__':
    boston = load_boston()
    data = pd.DataFrame(data=boston.data, columns=boston.feature_names)
    data['MEDV'] = boston.target
    data = data[data['MEDV'] != 50]
    X = data[["RM"]]
    y = data["MEDV"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=18)
    model = GDRegressor(alpha=0.04, n_iter=2000)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print(prediction)
    print(model.coef_, model.intercept_)
    rmse = rmse(prediction, y_test)
    r_squared = r_squared(prediction, y_test)
    print("RMSE = ", rmse)
    print("R_SQUARED = ", r_squared)
    data.plot(kind='scatter', x="RM", y="MEDV")
    plt.plot(X_train, model.coef_[0] * X_train + model.intercept_, 'r')
    plt.show()

