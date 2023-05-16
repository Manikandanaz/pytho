import json
import os
import fdl_util as util


filedir=os.path.dirname(os.path.realpath(__file__))
filedir1=os.path.dirname(os.path.abspath(__file__))
filedir2=os.getcwd()
conffile=os.path.join(filedir,util.base_basefileconfigname)
print(filedir)
print(conffile)
print(filedir1)
print(filedir2)

with open(conffile) as configfile:
    confdata = json.load(configfile)
print(confdata['dev']['DB_USER'])
