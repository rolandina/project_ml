import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self):
        self.titanic = self.__load_data_titanic()
        self.__preprocessing()
        y = self.titanic['survived']
        X = self.titanic.drop(columns=['survived'])
        X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    stratify=y,
                                                    random_state = 19 )

        self.__model = LogisticRegression(max_iter=1000)
        self.__model.fit(X_train,y_train)


    def __load_data_titanic(self):
        df = sns.load_dataset("titanic")
        titanic = df.drop(columns=['class', 'adult_male', 'embark_town', 'alive', 'deck', 'parch'])
        return titanic

    def __preprocessing(self):
        self.titanic['alone'] = self.titanic['alone'].replace([True, False], [1,0])
        self.titanic['adult'] = self.titanic['who'].replace(["man","woman", 'child'], [1,1,0])
        self.titanic = self.titanic.drop(columns=['who'])
        self.titanic['sex'] = self.titanic['sex'].replace(['male', 'female'], [1,0])
        self.titanic['embarked'] = self.titanic['embarked'].replace(['C', 'Q', 'S'], [0,1,2])
        self.titanic.replace(np.nan, np.mean(self.titanic[self.titanic['adult']==1]['adult']), inplace=True)

    #prediction
    def create_X_prediction(self, pclass, sex, age, sibsp, fare, embarked):
        # widgets limits
        # for col in self.titanic.columns[1:]:
        #     if len(self.titanic[col].unique())>5:
        #         print(f"{col}:[{self.titanic[col].min()}, {self.titanic[col].mean()} {self.titanic[col].max()}]")
        #     else:
        #         print(f"{col}:{self.titanic[col].unique()}")

        X_prediction = pd.DataFrame({col: [0] for col in self.titanic.columns[1:]})

        X_prediction.pclass = pclass#3
        X_prediction.sex = sex#0
        X_prediction.age = age#19
        X_prediction.sibsp = sibsp#2
        X_prediction.fare = fare#30
        X_prediction.embarked = embarked#1.
        X_prediction.alone = 1 if sibsp > 1 else 0
        X_prediction.adult = 1 if age > 18 else 0

        return X_prediction

    def prediction(self, X_prediction):
        result = self.__model.predict_proba(X_prediction)
        text_res = ""
        if result[0][0]>0.5:
            text_res = f"The passager is dead with probability {int(result[0][0]*100)}%" 
        else:
            text_res = f"The passager is survived with probability {int(result[0][1]*100)}%"

        return text_res

