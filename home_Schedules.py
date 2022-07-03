import pandas as pd


def homeScedules():
    maleList=[]
    femaleList=[]
    finalList=[]
    df = pd.read_csv("FinleTest.csv").fillna('').to_dict(orient='split')
    df2 = pd.read_csv("FemaleBranches.csv").fillna('').to_dict(orient='split')
    
    for i in df['data']:
        maleList.append({index: value for index, value in enumerate(i)})
    for i in df2['data']:
        femaleList.append({index: value for index, value in enumerate(i)})    
    finalList.append(maleList)
    finalList.append(femaleList)
    return finalList


homeScedules()
