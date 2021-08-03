from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, model, params=dict()):
        self.model = model
        self.model.set_params(**params)

    def get_model(self):
        return self.model, self.model.get_params()

    def score(self, X_train, X_test,  y_train, y_test):
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

    def predict(self, X_predict):
        return self.model.predict_proba(X_predict)