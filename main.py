import imp
from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from JUC_schedule_maker import scheduler
from home_Schedules import homeScedules
import json


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


@app.post('/')
async def JUCdata(inputData: List[Union[list, str]]):
    print('courses1',inputData[0])
    print('branch',inputData[1])
    return scheduler(inputData[0], inputData[1])  