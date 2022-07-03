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
    'https://juc-schedule.web.app/'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

coursesList: List[str] = []
branch: List[str] = []


@app.get('/')
async def root():
    return coursesList


@app.get('/scheduls')
async def root():
    TheList = scheduler(coursesList, branch[0])
    coursesList.clear()
    branch.clear()
    return TheList


@app.get('/home_scheduls')
async def root():
    return homeScedules()


@app.post('/')
async def courses_list(courses: List[Union[list, str]]):
    coursesList.clear()
    branch.clear()
    coursesList.append(courses[0])
    branch.append(courses[1])
    return scheduler(coursesList, branch[0])


@app.delete('/delete')
async def delete_list():
    coursesList.clear()
    branch.clear()
    return
