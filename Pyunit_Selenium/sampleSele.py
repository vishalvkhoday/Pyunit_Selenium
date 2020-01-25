'''
Created on Nov 9, 2019

@author: DELL
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Collection
from selenium.webdriver.remote.webdriver import WebDriver
# driver = webdriver.Chrome(executable_path='C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver_242')
driver = WebDriver(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=True,options=None)

driver.get("https://www.moneycontrol.com/")
welist = driver.find_elements(By.XPATH,("//div[@id]/div/ul/li"))

for i, ele in enumerate(welist):
    obj_driv = welist[i]
    print(ele .location)