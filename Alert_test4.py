'''
Created on Jan 29, 2019

@author: vkhoday
'''


from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


txt_scr ='//*[@id="search_str"]'

driver = webdriver.Chrome('C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/WebDriver/chromedriver_235')

driver.get('https://www.moneycontrol.com')
ActionChains(driver).pause(3)
driver.maximize_window()
driver.find_element_by_xpath(txt_scr).send_keys(Keys.ENTER)
txt_msg =Alert(driver).text
print(txt_msg)
Alert(driver).accept()

