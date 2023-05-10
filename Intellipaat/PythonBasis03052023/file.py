import os
print('the path is',os.path)
os.chdir('../')
file1 = open(".\\pytho\\Intellipaat\\PythonBasis03052023\\for.py", "rb")
print(file1.read())