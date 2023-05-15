import configparser as cf
config=cf.ConfigParser()
config.sections()
config.read('exampl.ini')
for key in config['SEC1']:  
    print(key)