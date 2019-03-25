'''
Created on Mar 19, 2019

@author: vkhoday
'''
from functools import reduce 
import re
import calendar
import openpyxl

import time


f = lambda x: 2 * x
print(f(3))


g = lambda x: x> 10
print(g(3))
print(g(11))

h =[1,2,3,4,5,6,7]
squarelist = map(lambda x: x*x,h)
sqval = []
for x in squarelist:
    print(x)
    sqval.append(x)    
    
def Greatnos(x):
    if x >=10 :
        return True
    else:
        return False
    
s_val = []
fil = filter(lambda x: x>10,sqval)
for y in fil:
    print(y)
    s_val.append(y)
    
s = reduce(lambda x,y: x*y,s_val)
print("\n\n\n",s)
    
Fam = ["Mom","Vishal","Vidya","Akruthi"]
AA = set(Fam)
AA.add("Vinayak")
AA.remove("Vishal")
diff=AA.difference(Fam)
print (AA)
for A in AA:
    print(A)
    
Ab = set(["a","b","c","d"])
Ac = set(["b","c"])
print(Ac.issubset(Ab))
print(Ab.issuperset(Ac))
print(Ab.intersection(Ac))

nums = [1,2,3,450,5,6,7,8,375]
names = ["Mom","Vinayak","Khoday","Akruthi"]
names_hui = max(names)
names.sort(key=None, reverse=False)
for n in names:
    print(n)
high =max(nums)
nums.sort(key=None, reverse=True)
print(nums[1],high)
for x in nums:
    print(x)
    
def sumDigit(num1):
    sum=0
    while(num1):
        sum+= num1 % 10
        num1 = int(num1/10)
    return sum

print("Maximum is : ", max(100, 321, 267, 59, 40,key=sumDigit))
num1 = [1,2,3,450,5,6,7,8,375]
print("Maximum is : ",max(num1,key=sumDigit))

iter_num = iter(num1)
print(iter_num)
while True:
    try:
        print(next(iter_num))
    except:
        break
    
strmssg ="Python is intersting."
arr=bytes(strmssg,'utf-8')
print(arr)

string1 = "python is awesome, isnt it?"
substr1 = "n"
cnt = string1.count(substr1)
print("the occurance {}".format(cnt))
res = re.findall(r'[is]\w', string1)
print("next occurance {}".format(len(res)))


def CreateGen():
    mylist =range(12)
    for i in mylist:
        yield i*i
genlist =[]
no_list =[]
gen_num =CreateGen()
for xx,abc in enumerate(gen_num,start=1):
    print(xx,abc)
    genlist.append(abc)
    no_list.append(xx)
    print(genlist.count(abc))
no_list.extend(genlist)
no_list.sort(key=None, reverse=False)
print(no_list)
uni_list=[]
for a in no_list:
    if a not in uni_list:
        uni_list.append(a)
        
for b in uni_list:
    print("Occurance of {} is {} times".format(b,no_list.count(b)))

print ("Highest nos in the list {}".format(max(genlist)))
print ("Lowest nos in the list {}".format(min(genlist)))

print(no_list[::-1])
str_name = "Vishal"
print(str_name[::-1])

with open("WebDriver/file_x.txt","w+") as f1:
    f1.write("This is test file for reference")
    f1.close()
scr_list = []
dict_scrname = {}
scr ='Script'
Wb = openpyxl.load_workbook("WebDriver/Down_Scripts_List.xlsx")
Ws= Wb['Sheet1']
row_cnt = Ws.max_row
for ii in range(2,10):
    scr_name = Ws[str('A')+str(ii)].value
    print(scr_name)
    scr_list.append(scr_name)
    dict_scrname.update({scr_name:scr})
    if ii ==15:
        break
insItem= dict_scrname.items()
str_Val =dict_scrname.values()
str_key = dict_scrname.keys()
dict_scrname.get('20MICRONS')
print(insItem,str_Val,str_key)
    
    