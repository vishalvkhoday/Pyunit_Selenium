'''
Created on Jan 2, 2019

@author: vkhoday
'''

from numpy.random import rand
from numpy.random.mtrand import randint
from pandas.DataFrame import *
import pandas

for i in range(0,10):
    r =randint(26,size=(5,10))
    print (r)
    
pd = pandas.Series(randint.random.randn(50))
