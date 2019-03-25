'''
Created on Jan 31, 2019

@author: vkhoday
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Test_1 import driver
import time
from selenium.webdriver.common.by import By

driver.get('http://www.globalsqa.com/demo-site/draganddrop/')
# driver.get('https://jqueryui.com/droppable/')
driver.set_page_load_timeout(3)
driver.maximize_window()
iframe = driver.find_element_by_xpath('//*[@id="post-2669"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(iframe)
img_scr = driver.find_element_by_xpath('//*[@id="gallery"]/li[1]/img')
img_dest = driver.find_element_by_xpath('//*[@id="trash"]')


ActionChains(driver).drag_and_drop(img_scr,img_dest).perform()
ActionChains(driver).pause(5)
time.sleep(5)
driver.quit()