'''
Created on Jan 2, 2019

@author: vkhoday
'''

from numpy.random import rand
from numpy.random.mtrand import randint
import pandas

from selenium import webdriver

dr =webdriver.Chrome(executable_path='C:/Users/DELL/git/Pyunit_Selenium/WebDriver/chromedriver_235')

dr.get("https://www.google.com")
y =dr.execute_script("return document.body.scrollHeight")
x =dr.execute_script("return document.body.scrollWidth")
print(x,y)

for i in range(0,10):
    r =randint(26,size=(5,10))
    print (r)
    
pd = pandas.Series(randint.random.randn(50))
