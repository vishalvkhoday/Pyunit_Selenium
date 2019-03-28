'''
Created on Dec 28, 2018

@author: vkhoday
'''
import os
import  datetime
import random
from selenium.common.exceptions import ElementClickInterceptedException
import allure
import pytest
import socket
# for i in range(1,5):
#     try:
#         os.system('python C:/Users/vkhoday/eclipse-workspace/Bse_Results_extractor/src/Bse_Extractor_V1.py')
#         print(i)
#         time.sleep(10)       
#     except:
#         continue

class Person():
    
    def __init__(self,name,age):
        self.name =name
        self.age = age
    @pytest.mark.xfail(condition = lambda : True ,reason='This is expected failure')
    def Test_Fail_scenario(self):
        try:
            print("Expected failure")
            assert False
        except  AssertionError as ae:
            print(ae)
    def Test_Pass_scenario(self):
        try:
            print("Expected Pass")
            assert True
        except  AssertionError as ae:
            print(ae)
    
    @pytest.fixture
    def Test_function(self,Req):
        raise Exception('This is wrong nos')
        
        
        
            
P = Person('Vishal',37)
senten = 'name is {0.name} & his age is {0.age}'.format(P)
print (senten)

dict_per = {'name':'Vishal v khoday','age':37}

sent = 'This person is {name} and his age {age}'.format(**dict_per)

print(sent)

print ('The value of 1 MB will is = {:,.2f}'.format(1024**2))

print('Today date is {:%F,%S}'.format(datetime.datetime.now()))

cs_course ={'History','Social','Math','CompSci','History'}
Art_course = {'Art','Design','Math','History'}
cs_course=cs_course.union(Art_course)


for i,j in enumerate(cs_course,start=10):
    print (i,j)
print(cs_course.union(Art_course))
print(sorted(cs_course))


greeting =['Hello','Hi','Howdy','Halo','Hi']

wish = random.choices(greeting,k=15)

print(wish )

deck = list(range(1,52))

random.shuffle(deck)
try:
    print (deck)
except ZeroDivisionError:
    None


print(random.sample(deck,k=5))

test_sent = 'This is the test msg to display'
print (test_sent.split()[1])
P.Test_Fail_scenario()
P.Test_Pass_scenario()