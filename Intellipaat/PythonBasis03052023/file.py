import os
import sys
import subprocess
os.chdir('../pytho/Intellipaat/PythonBasis03052023/')
dir= os.getcwd()
file1 = open(sys.argv[1], "rb")
Lines = file1.readlines()
count = 0
ls=('Connect-AzAccount -Tenant "cb2cd16c-339b-4d56-9133-8c26c0c5a4f0"')
for line in Lines:
    count += 1
    line=line.decode('ASCII')
    filepath=str(dir)+'\\'+str(line).rstrip()
    filename =str(line.replace('.json','').rstrip())
    print(filename)
    #print('the file path is '+filepath.replace("\\","\\\\"))
    #filepathtxt=open(filepath,"r")
    #mytextline=str(filepathtxt.readlines())[1:-1].replace("'","")
    cmd='\n '+'Set-AzDataFactoryV2Pipeline -DataFactoryName '+'"'+sys.argv[3]+'"'+' -ResourceGroupName '+'"'+sys.argv[2]+'"'+' -Name '+'"'+filename+'"'+' -DefinitionFile '+'"'+filepath+'"'+' -Force'
    ls=ls+cmd
print(ls)
    #print("Line{}: {}".format(count, line.strip().decode('ASCII')))
ps_command = ls
process = subprocess.Popen(['powershell', '-Command', ps_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# print the output and errors
print(output.decode())
print(error.decode())
