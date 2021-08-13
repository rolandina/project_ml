from fastapi import FastAPI, Path, HTTPException
#import uvicorn
#import os

from titanic.model import Model
from enum import Enum

# load environment variables
#port = os.environ["PORT"]


app = FastAPI(title="Titanic")

class Sex(str, Enum):
    male = "male"
    female = "female"

class Embarked(str, Enum):
    Q = "Q"
    S = "S"
    C = "C"

class Pclass(str, Enum):
    first = 1
    second = 2
    third = 3

@app.get("/prediction/",
    response_description ="""{
  "result": 1,
  "text_result": "survived",
  "probability": 69,
  "description": "The passager survived with probability 69%"
}""",
    description="/prediction/?pclass={pclass}&sex={sex}&age={age}&sibsp={sibsp}&fare={fare}&embarked={embarked} takes 6 parameters and \
    return the answer if passager died or survived",
)
async def prediction(pclass: Pclass, sex: Sex, age: float, sibsp: int, fare: float, embarked: Embarked):

    m = Model()
    return m.predict(m.create_X_prediction(pclass,sex,age,sibsp,fare,embarked))
    


@app.get("/model_description/",
        response_description = """{
  "model": "LogisticRegression",
  "params": {
    "C": 1,
    "class_weight": null,
    "dual": false,
    "fit_intercept": true,
    "intercept_scaling": 1,
    "l1_ratio": null,
    "max_iter": 1000,
    "multi_class": "auto",
    "n_jobs": null,
    "penalty": "l2",
    "random_state": null,
    "solver": "lbfgs",
    "tol": 0.0001,
    "verbose": 0,
    "warm_start": false
  }
}""",
        description = "Returns name and the parameters of the model to use in prediction."
        )
async def description():
    m = Model()
    return m.get_model()


@app.get("/list_models/",
        response_description = """{
  "models": [
    "LogisticRegression",
    "DecisionTreeClassifier",
    "KNeighborsClassifier"
  ]
}
""",
        description = "Returns list of models ready to use for titanic data set"
        )
async def list_all_models():
    m = Model()
    return m.get_models_list()
    

@app.get("/raw_data/",
        response_description = "pandas data frame in json format",
        description = "Returns data frame titanic in json format."
        )
async def get_raw_data():
    return Model().titanic.to_json(orient= 'columns')


# if __name__=='__main__':
#     uvicorn.run("api:app", host="0.0.0.0", port = port, reload=False)