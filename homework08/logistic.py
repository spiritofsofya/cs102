import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split


class LogisticRegression:
    def __init__(self, alpha=0.001, max_iter=5000):
        self.alpha = alpha
        self.max_iter = max_iter

    def fit(self, X_train, y_train):  # Обучение и тренировка модели
        m = y_train.size
        X = X_train.copy()
        X = np.insert(X, 0, 1, axis=1)
        t = X.T
        theta = np.zeros(X.shape[1])

        for n in range(self.max_iter):
            z = np.dot(theta, t)
            sigma = 1 / (1 + np.exp(-z))
            theta -= self.alpha * (1 / m) * np.dot((sigma - y_train), X)

        self.intercept_ = theta[0]
        self.coef_ = theta[1:]

        return self.coef_, self.intercept_

    def predict(self, X_test):  # Возвращение прогнозов для новых данных
        pred = []
        for i in range(len(X_test)):
            z = self.intercept_ + np.sum(X_test[i] * self.coef_)
            sigma = 1 / (1 + np.exp(-z))

            if sigma >= 0.5:
                pred.append(1)
            else:
                pred.append(0)

        return pred

    def predict_proba(self, X_test):
        return [(1 / (1 + np.exp(-(self.intercept_ + np.sum(X_test[i] * self.coef_)))), 1 - 1 /
                 (1 + np.exp(-(self.intercept_ + np.sum(X_test[i] * self.coef_))))) \
                for i in range(len(X_test))]


if __name__ == '__main__':
    data = datasets.load_iris()

    X = data.data[:100, :2]
    y = data.target[:100]

    setosa = plt.scatter(X[:50, 0], X[:50, 1], c='orange')
    versicolor = plt.scatter(X[50:, 0], X[50:, 1], c='blue')
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.legend((setosa, versicolor), ("Setosa", "Versicolor"))
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=17)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    answers = model.predict(X_test)
    probabilities = model.predict_proba(X_test)
    print(answers)
    print(probabilities)
