'''
Created on Mar 21, 2019

@author: vkhoday
'''

import re
import urllib

sample = "This is the second work in this work 28484 8294 238982 !! 3###4-39485@@@"

matchObj = re.search(r'\w', sample,re.M|re.I)
if matchObj:
    for i in range(1,5):
        print(matchObj)