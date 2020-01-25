'''
Created on Dec 12, 2019

@author: DELL
'''
from PIL import Image
import numpy as np
import os
from time import strftime, strptime
from datetime import datetime 

Img_path = '../Pyunit_Selenium/Screen_shot/'
list_img =os.listdir(Img_path)


# list_img=['../Pyunit_Selenium/Screen_shot/20190116182806.png','../Pyunit_Selenium/Screen_shot/20190116173701.png','../Pyunit_Selenium/Screen_shot/20190116175307.png']
dtstp = datetime.now().strftime("%Y%m%d%H%M%S")
imgs = [Image.open(Img_path+i) for i in list_img]
min_shape =sorted([(np.sum(i.size),i.size) for i in imgs])[0][1]
imgs_comb = np.vstack((np.array(i.resize(min_shape)) for i in imgs))
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('../Pyunit_Selenium/Screen_shot/Merge{}.png'.format(dtstp))
print("Done")
