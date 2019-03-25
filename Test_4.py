'''
Created on Jan 31, 2019

@author: vkhoday
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Test_1 import driver

from allure import step

driver.get('https://moneycontrol.com')
driver.set_page_load_timeout(4)
driver.maximize_window()
step(driver.title)
hm_but = driver.find_element_by_xpath('//*[@title="Submit"]')
ActionChains(driver).click(hm_but)
ActionChains(driver).pause(3)


