from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, model, params=dict()):
        self.model = model
        self.model.set_params(**params)

    def fit_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def get_model(self):
        return {'model': str(self.model).split('(')[0], 'params': self.model.get_params()}

    def score(self, X_train, X_test,  y_train, y_test):
        self.model.fit(X_train, y_train)
        return self.model.score(X_test, y_test)

    def predict(self, X_predict):
        result = self.model.predict_proba(X_predict)
        prob = int(result[0][0] * 100)
        output = dict()
        if prob >= 50:
            output['result'] = 0
            output['text_result'] = 'died'
        else:
            prob = 100 - prob
            output['result'] = 1
            output['text_result'] = 'survived'

        output['probability'] = prob
        output['description'] = f"The passager {output['text_result']} with probability {prob}%"
        return output
