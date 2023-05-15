import configparser as cf
config=cf.ConfigParser()
config['Default']={'ServerAliveInterval': '45','Compression': 'yes','CompressionLevel': '9'}
config['secion1']={}
config['secion1']['user']='hg'
config['top secret']={}
topsecret=config['top secret']
topsecret['port']='32'
with open('exampl.ini','w') as configfile:
    config.write(configfile)
    

