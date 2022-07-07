import imp
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from JUC_schedule_maker import scheduler
from home_Schedules import homeScedules
import pandas as pd
import numpy as np


app = FastAPI()

origins = [
    'https://juc-schedule.web.app/',
    'http://localhost:3000/'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home_scheduls')
async def root():
    return homeScedules()

@app.post('/check')
async def JUCcourses(inputData: List[Union[list, str]]):
    if inputData[1] == '1':
        # read master schedule
        df = pd.read_csv("FinleTest.csv")
    elif inputData[1] == '2':
        df = pd.read_csv("FemaleBranches.csv")
    print(np.isin(inputData[0],df['Course Code'].unique()))
    return (np.isin(inputData[0],df['Course Code'].unique())).tolist()  

@app.post('/')
async def JUCdata(inputData: List[Union[list, str]],page_num: int=1, page_size: int=5):
    data=scheduler(inputData[0], inputData[1])
    # print(data.__len__())
    start = (page_num-1)*page_size
    end=start+page_size
    # print('courses1',inputData[0])
    # print('branch',inputData[1])
    return data[start:end],data.__len__()