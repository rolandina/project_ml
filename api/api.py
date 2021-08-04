from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
from fastapi import HTTPException
import uvicorn
import pandas as pd
import json
from titanic.data import Data
from titanic.model import Model
from enum import Enum
from sklearn.linear_model import LogisticRegression

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
    
    d = Data()
    X_train, X_test, y_train, y_test = d.get_prepared_data()
    m = Model(LogisticRegression(), {'max_iter': 1000})
    m.fit_model(X_train, y_train)
    return m.predict(d.create_X_prediction(pclass,sex,age,sibsp,fare,embarked))
    


@app.get("/model_description/")
async def description():
    d = Data()
    X_train, X_test, y_train, y_test = d.get_prepared_data()
    m = Model(LogisticRegression(), {'max_iter': 1000})
    m.fit_model(X_train, y_train)
    return m.get_model()
    
#@app.get("/raw_data/") #????


