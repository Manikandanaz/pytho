#To list python installed version we can use py launcher utility in windows
#In cmd "py -0/py --list" will tell u the list of python version installed
#In cmd "py -3.10/py -3.11" command will force the code to execute in particular version

#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))