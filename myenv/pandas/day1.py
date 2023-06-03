import pandas as pd
import os
os.chdir("./myenv/pandas/")
fd=pd.read_csv("testdata.csv")
rd=pd.DataFrame(
    {
        "Name":["mani","mani","ajay","javeed","javeed"],
        "Age":[10,10,50,45,None]  
    })
#print(rd.head(3))
#print(rd.tail(2))
#print(rd["Name"])#series
#print(rd.columns)
#print(rd.keys())
#print(rd.shape)
sd=pd.Series([23,45,'mani'],name="age")#create series only values
#print(sd.keys)
#print(rd.nunique())
#print(rd.ndim)
#print(rd.size)
#print(rd.duplicated().sum())
#print(fd.isnull().sum())
#print(rd["Age"].describe())
