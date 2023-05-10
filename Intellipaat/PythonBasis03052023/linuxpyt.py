import os
import sys
import subprocess
dir= os.getcwd()
file1 = open(sys.argv[1], "rb")
Lines = file1.readlines()
count = 0
ls=('Connect-AzAccount -Identity')
for line in Lines:
    count += 1
    line=line.decode('ASCII')
    filepath=str(line).rstrip()
    filename=str(line.replace('.json','').rstrip())
    cmd='\n '+'Set-AzDataFactoryV2Pipeline -DataFactoryName '+'"'+sys.argv[3]+'"'+' -ResourceGroupName '+'"'+sys.argv[2]+'"'+' -Name '+'"'+filename+'"'+' -DefinitionFile '+'"'+filepath+'"'+' -Force'
    ls=ls+cmd
print(ls)
ps_command=ls
process=subprocess.Popen(['/usr/bin/pwsh', '-Command', ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
print(output.decode())
print(error.decode())