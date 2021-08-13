import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


class Data:
    def __init__(self):
        self.titanic = self.__load_data_titanic()
        self.X_train, self.X_test, self.y_train, self.y_test = self.get_prepared_data()

    def get_prepared_data(self):
        """return X_train, X_test, y_train, y_test prepared for the model"""
        df = self.__preprocessing(self.titanic.copy())
        y = df['survived']
        X = df.drop(columns=['survived'])
        return train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 19)

    def __load_data_titanic(self):
        df = sns.load_dataset("titanic")
        titanic = df.drop(columns=['class', 'adult_male', 'embark_town', 'alive', 'deck', 'parch', 'who'])
        return titanic

    def __preprocessing(self, df):
        # create preprocessing pipeline instead!
        ## 1 = True; 0 = False 
        df['alone'] = df['alone'].replace([True, False], [1,0])
        df['sex'] = df['sex'].replace(['male', 'female'], [1,0])
        df['embarked'] = df['embarked'].replace([np.nan], [df['embarked'].mode()])
        df['embarked'] = df['embarked'].replace(['C', 'Q', 'S'], [0,1,2])
        df['age'] = df['age'].replace(np.nan, np.mean(df[df['age']>15]['age']))
        return df

    #prediction

    def x_data_range(self):
        """return dictionary with name of the columns as keys and range or tuple for values"""
        range = dict()
        for col in self.titanic.columns:
            if len(self.titanic[col].unique())>5:
                range[col] = (self.titanic[col].min(), self.titanic[col].max(), self.titanic[col].mean())
            else:
                range[col] = tuple(self.titanic[col].unique())
        return range

    def create_X_prediction(self, pclass, sex, age, sibsp, fare, embarked):

        X_prediction = pd.DataFrame({col: [0] for col in self.titanic.columns[1:]})

        X_prediction.pclass = pclass#3
        X_prediction.sex = sex#"male" or "female"
        X_prediction.age = age#19
        X_prediction.sibsp = sibsp#2
        X_prediction.fare = fare#30
        X_prediction.embarked = embarked#'S', 'Q', 'C'
        X_prediction.alone = 1 if sibsp > 1 else 0
    
        return self.__preprocessing(X_prediction)
