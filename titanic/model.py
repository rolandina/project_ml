from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from titanic.data import Data


class Model(Data):
    # dictionary of all models avalable in 
    __models_dict = {'LogisticRegression': [LogisticRegression(), {'max_iter': 1000}],
                    'DecisionTreeClassifier': [DecisionTreeClassifier(), dict()],
                    'KNeighborsClassifier': [KNeighborsClassifier(), dict()]
    }


    def __init__(self):
        super().__init__()
        self.model = self.__models_dict['LogisticRegression'][0]
        params = self.__models_dict['LogisticRegression'][1]
        self.model.set_params(**params)
        self.model.fit(self.X_train, self.y_train)

    def get_models_list(self):
        return {'models' : list(self.__models_dict.keys())}
    
    def get_model(self):
        return {'model': str(self.model).split('(')[0], 'params': self.model.get_params()}

    def score(self):
        return self.model.score(self.X_test, self.y_test)

    def predict(self, X_predict):
        result = self.model.predict_proba(X_predict)# 0 - dead [[0.34,0.66]]  1- alive
        prob = int(result[0][0] * 100) #34 %  
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
