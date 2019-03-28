'''
Created on Mar 18, 2019

@author: vkhoday
'''
import configparser
from cryptography.fernet import Fernet
import datetime

config=configparser.ConfigParser()
f_dt = str(datetime.datetime.now()).replace(":","").replace(" ","_").replace(".","_")
config.read("WebDriver/config.ini")
config.sections()
urID =config['bitbucket.org']['User']
crypt_key = config['bitbucket.org']['key']
pwd=config['bitbucket.org']['pwd']

print(urID,"\nKey:",crypt_key,"\nPassword:",pwd)
key= Fernet.generate_key()
cipherSuit =Fernet(crypt_key)
# cipherSuit =Fernet(key)
# cipherText= cipherSuit.encrypt(b"Password")
plainTxt = cipherSuit.decrypt(bytes(pwd,'utf-8'))
print(crypt_key)
# print(cipherText)
print(plainTxt)

# with open("WebDriver/keys_{}.txt".format(f_dt),"w+")as file1:
#     file1.write("Key: "+str(crypt_key))
#     file1.write("\nPassword: "+str(pwd))
#     file1.write("\n"+str(plainTxt))
#     file1.close()