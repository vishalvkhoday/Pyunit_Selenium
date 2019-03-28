'''
Created on Mar 18, 2019

@author: vkhoday
'''

import configparser
from cryptography.fernet import Fernet
config=configparser.ConfigParser()
key= Fernet.generate_key()
cipherSuit =Fernet(key)
cipherText= cipherSuit.encrypt(b"Password")

config['DEFAULT']={'ServerAliveInterval':'45','Compression':'Yes','CompressionLevel':'9'}

config['bitbucket.org']={}
config['bitbucket.org']['User']='hg'
# config['bitbucket.org']['Pwd']= 'gAAAAABcj3L7DshJO4TD5lJQhtcJZ5wNPDjkTG5-9Fc6vpEzmh5BVpGAOvU3lTt_Ot6W77iX6ylvGQjh8ACO2m8Bxtl0A8WrtA=='
config['bitbucket.org']['Pwd'] = str(cipherText,'utf-8')
config['bitbucket.org']['Key']=str(key,'utf-8')
config['topsecret.com']={}

with open("WebDriver/config.ini","w+") as configFile:
    config.write(configFile)
    
print("Done successfully")