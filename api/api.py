from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
from fastapi import HTTPException
import uvicorn
import pandas as pd
import json
from titanic.data import Data


app = FastAPI(title="Titanic")

@app.get("/prediction/",
    response_description ="{'answer': 'The passanger is dead with probability 68%'}",
    description="/prediction/?pclass={pclass}&sex={sex}&age={age}&sibsp={sibsp}&fare={fare}&embarked={embarked} takes 6 parameters and \
    return the answer if passager is dead or alive",
)
async def prediction(pclass: int, sex: int, age: float, sibsp: int, fare: float, embarked: int):
    
    d = Data()
    m = Model()
    res = m.prediction(d.create_X_prediction(pclass,sex,age,sibsp,fare,embarked))
    #return {'answer': text_result}
    return [{f"result: {res}, result_text:{} probability:{text_result}, description:{text_result}"}]

#@app.get("/model_description/")
#@app.get("/raw_data/") #????


