import pandas as pd
import os
os.chdir("./myenv/pandas/")
fd=pd.read_csv("testdata.csv")
rd=pd.DataFrame(
    {
        "Name":["mani","mani","ajay","javeed","javeed"],
        "Age":[10,10,50,45,None]  
    })
##SHOULD DO USE PARENTHESIS FOR ATTRIBUTES
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
#print(rd["Age"].isnull().sum())
#print(rd["Age"].notna())
td=pd.DataFrame(rd["Age"].fillna('hi i am for null'))
print(td.columns)
#installed openpyxl module to export operation
#td.to_json("hi1frompy.json",indent=1,index='orient')
#print(type(td["Age"]))
#print(td["Age"].shape)
#print(rd[["Age","Name"]])
#print(rd[(rd["Age"].isin([10.00])) | (rd["Name"]=="mani11")])
#print(rd[(rd["Age"].isin([10.00])) & (rd["Name"]=="mani11")])
#print(rd.loc[rd["Name"]=="mani","Age"])#select particular column
#print(fd.describe)
#print(fd.info())

#   
# print (fd[(fd["Schooling"]>6) & (fd["Gender"]==1)])
#print (fd[(fd["Spinal_Cord_MRI"])==1])
print(fd.loc[1:3,2])