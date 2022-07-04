from typing import List
import pandas as pd
import numpy as np
import itertools
import json


def scheduler(coursesList: List[str], branch: str):
    print(type(branch))
    coursesList = coursesList[-1]

    if branch=='1':
        # read master schedule
        df = pd.read_csv("FinleTest.csv")
    elif branch=='2':    
        df = pd.read_csv("FemaleBranches.csv")

    # group every course code in data frame
    groupCC = df.groupby(['Course Code'])

    # iterate in each data frame
    allCourses = []
    for course, courses_df in groupCC:
        allCourses.append(course)

    # print(coursesList)

    # user input courses
    coursesDict = {}
    for ele in coursesList:
        # pass the course code or index in the allCourses
        newDf = groupCC.get_group(ele)
        # times column access
        times = newDf.iloc[:, 7:12].values
        SCs = newDf.iloc[:, 5].unique()
        coursesDict[ele] = list(SCs)

    # print(coursesDict)                              #dict with all users courses and scs

    keys, values = zip(*coursesDict.items())
    combList = [dict(zip(keys, v))for v in itertools.product(
        *values)]  # all combination of the secs and courses
    # print(combList)
    validDF_lists = list()
    validDF_dict = dict()
    for dict_iteam in combList:
        daysDict = {}
        daysDict_after = {
            'SUN': [],
            'MON': [],
            'TUE': [],
            'WED': [],
            'THU': []
        }
        isVaild = True
        finledf = pd.DataFrame(columns=['Course Code', 'Course name', 'CR', 'CT', 'S. Seq',
                               'SC', 'Activity', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'Room No', 'STAFF'])
        for course in dict_iteam:
            counter = 0
            # print(course,'->',dict_iteam[course])       #couse code, sec num
            groupEach = df.groupby(['Course Code', 'SC'])

            # iterate over the values (scs) of the dict to gather the practical and theoretical sec
            courseDf = groupEach.get_group((course, dict_iteam[course]))
            # print(courseDf)

            days = ['SUN', 'MON', 'TUE', 'WED', 'THU']
            daysDict = {
                'SUN': [],
                'MON': [],
                'TUE': [],
                'WED': [],
                'THU': []
            }
            for day in days:
                daysDict[day] = courseDf[day].tolist()
                for i in daysDict[day]:
                    if not type(i) == float:
                        daysDict[day] = i.split(',')
                daysDict_after[day] += [int(i)
                                        for i in daysDict[day] if not type(i) == float]
                # check if theres a duplicate number in each day
                if len(daysDict_after[day]) != len(set(daysDict_after[day])):
                    isVaild = False
            # print(daysDict_after)
            if isVaild:
                finledf = pd.concat([courseDf, finledf], ignore_index=True)
            counter += 1
        # print(isVaild)
        if isVaild:
            finledf = finledf.fillna('')
            validDF_lists.append(finledf.to_dict(orient='split'))
            # validDF_dict[counter]=finledf.to_dict

        # after finish the inner loop
        # if list == set then store the dataframe in the list
    # print('Number of valid schedule: ',len(validDF_lists))
    # for validdf in validDF_lists:
    #     print(validdf)                      # print all valid df
    # jsonDf=json.dumps(validDF_lists)
    return validDF_lists
