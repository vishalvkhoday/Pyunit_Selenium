'''
Created on Sep 12, 2019

@author: DELL
'''
import numpy as np
import matplotlib.pyplot as plt

arr =np.random.randint(1,15,(6,5))
print (arr)
print(arr.max())
print (arr.min())
arr1 = np.random.random(1)
print (arr1)
arr2 = np.random.rand(10,10)
arr3 = np.random.randint(1,10,(10,10))

print (arr2+arr3)
plt.imshow(arr3)
plt.show()