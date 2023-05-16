import json
import os
import fdl_util as util
filedir=os.path.dirname(os.path.realpath(__file__))
filedir1=os.path.dirname(os.path.abspath(__file__))
filedir2=os.getcwd()
conffile=os.path.join(filedir,util.base_basefileconfigname)
with open(conffile) as configfile:
    confdata = json.load(configfile)
print(confdata['dev']['DB_USER'])
buildfilepath=os.path.join(filedir2,confdata['dev']['BUILD_FOLDER'])
buildfile=os.path.join(filedir2,confdata['dev']['BUILD_FOLDER'],confdata['dev']['BUILD_FILE'])
try:
    os.chdir(buildfilepath)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
print('the current dir is',os.getcwd())
print(buildfilepath)
print(buildfile)