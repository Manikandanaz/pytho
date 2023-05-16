import json
import os
import fdl_util as util


filedir=os.path.dirname(os.path.realpath(__file__))
conffile=os.path.join(filedir,util.base_basefileconfigname)
print(filedir)
print(conffile)

with open(conffile) as configfile:
    confdata = json.load(configfile)

print(confdata['dev']['DB_USER'])
