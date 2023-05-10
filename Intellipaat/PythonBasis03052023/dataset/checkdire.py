import inspect, os
print (inspect.getfile(inspect.currentframe())) # script filename (usually with path)
sourcepath= (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) # script directory
if sourcepath.endswith('dataset') == True:
    print('yes')
elif sourcepath.endswith('pipeline') == True:
    print('No')

  cmd='\n '+'Set-AzDataFactoryV2Pipeline -DataFactoryName '+'"'+sys.argv[3]+'"'+' -ResourceGroupName '+'"'+sys.argv[2]+'"'+' -Name '+'"'+filename+'"'+' -DefinitionFile '+'"'+filepath+'"'+' -Force'