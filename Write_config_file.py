'''
Created on Mar 18, 2019

@author: vkhoday
'''

import configparser
config=configparser.ConfigParser()
config['DEFAULT']={'ServerAliveInterval':'45','Compression':'Yes','CompressionLevel':'9'}

config['bitbucket.org']={}
config['bitbucket.org']['User']='hg'
config['bitbucket.org']['Pwd']= b'gAAAAABcj3L7DshJO4TD5lJQhtcJZ5wNPDjkTG5-9Fc6vpEzmh5BVpGAOvU3lTt_Ot6W77iX6ylvGQjh8ACO2m8Bxtl0A8WrtA=='
config['bitbucket.org']['Key']='UlR2LFw0y85SmCTf6iPfh3oRPON0EvqRyX2zwJSqLSg='
config['topsecret.com']={}

with open("WebDriver/config.ini","w+") as configFile:
    config.write(configFile)