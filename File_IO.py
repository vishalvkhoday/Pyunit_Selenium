'''
Created on Mar 18, 2019

@author: vkhoday
'''
import datetime
now = datetime.datetime.now()


f_dt = str(datetime.datetime.now()).replace(":","").replace(" ","_").replace(".","_")
print("{}".format(f_dt))
with open ("WebDriver/test.txt".format(f_dt),"r+") as f:
    print(f.name)
    print(f.close)
    print(f.closed)
    print(f.mode)
    while True:        
        data=f.read()
        if len(data)==0:
            break
        print(data)
    f.write("This is test msg {}\n".format(f_dt) *20)

    f.close()
    print(f.closed)



    
  