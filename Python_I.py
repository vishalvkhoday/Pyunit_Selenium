'''
Created on Mar 16, 2019

@author: vkhoday
'''
# number = [1,8,9,2,11,3,4,5,12,6,7,9]
# number.sort(key=None, reverse=True)
# print(number[1])
from builtins import isinstance 
age = [5, 12, 17, 18, 24, 32,33]
dict1 = {"name":"vishal","name":"Anil"}
sets1 = {"name:vishal","name:Anil"}
sets2 = {1,2,2,3,4,4}


def myFunc(x):    
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, age)
for x in adults:
    print (x)

a=1.0
b=1
c=1j

print(type(a))
print(type(b))
print(type(c))
print(type(dict1))
print(type(age))
print(type(sets1))
print(type(sets2))
print(sets2[1])
print(isinstance(age,list))
print(isinstance(dict1, dict))

