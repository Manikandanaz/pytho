import json

def myfun(a):
    if a==1:
         var=90
    else:
         var=100
    return var

jsonfile=open("myenv/sample.json","r")
data=json.load(jsonfile)
#print(data)
print('the',data["properties"]["connectVia"].V02alues())
data["properties"]["connectVia"]="rvsi"
print(data)