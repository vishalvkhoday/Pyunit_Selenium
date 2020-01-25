'''
Created on Jan 29, 2019

@author: vkhoday
'''

from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common import desired_capabilities
import unittest

desired_capabilities  = webdriver.DesiredCapabilities.CHROME
desired_capabilities['version']='latest'
desired_capabilities['platform']='WINDOWS'
desired_capabilities['name']= 'Test Selenium'
Options = ChromeOptions()
Options.add_argument("start-maximized")
Options.add_argument("disable-infobars")

xpath_App_Sec = '//*[@id="footer-sitemap-policy-content-content"]/div/ul/li[1]/a'
# driver = webdriver.Chrome(chrome_options=Options,executable_path="WebDriver/chromedriver_235")
driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor='http://localhost:4444/wd/hub')
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