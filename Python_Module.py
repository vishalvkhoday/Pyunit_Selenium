'''
Created on Mar 19, 2019

@author: vkhoday
'''

import sys
import datetime
import pymssql
import selenium.webdriver
import enum

for x in dir(sys):
    print(x)
print("\n***************************")
    
for y in dir(datetime):
    print(y)
print("\n***************************")
for z in dir(pymssql):
    print(z)
print("\n***************************")
a_a =[]
for a in dir(selenium.webdriver):
#     print(a)
    a_a.append(a)
a_a.sort(key=None, reverse=False)

print(a_a)
inputA = int('0101',2)
 
print ("Before shifting " + str(inputA) + " " + bin(inputA))
print ("After shifting in binary: " + bin(inputA << 1))
print ("After shifting in decimal: " + str(inputA << 1))

print(list(enumerate(a_a,start=1)))

for xx,yy in enumerate(a_a,start=1):
    print(xx,yy)


