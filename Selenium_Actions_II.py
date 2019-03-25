'''
Created on Mar 15, 2019

@author: vkhoday
'''

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://google.com')
element = driver.find_element_by_link_text('About')

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()

time.sleep(10) # Pause to allow you to inspect the browser.

driver.quit()