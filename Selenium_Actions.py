'''
Created on Jan 29, 2019

@author: vkhoday
'''


import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

xpath_App_Sec = '//*[@id="footer-sitemap-policy-content-content"]/div/ul/li[1]/a'
driver = webdriver.Chrome()

driver.get('https://google.com')
time.sleep(5)
element = driver.find_element_by_link_text('About')
element.click()
driver.maximize_window()
AppSec = driver.find_element_by_xpath(xpath_App_Sec)
# element.location_once_scrolled_into_view
# ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
# ActionChains(driver).double_click(element).move_by_offset(20,30).perform()
# ActionChains(driver).move_by_offset(456, 356).perform()
time.sleep(5)
AppSec.location_once_scrolled_into_view

time.sleep(10) # Pause to allow you to inspect the browser.

driver.quit()