from selenium import webdriver
from pytest import fixtures
from allure import *


driver = webdriver.Chrome(executable_path='WebDriver/chromedriver_235')

driver.get('https://www.bseindia.com')
# driver.find_element_by_xpath("//*[@id=='cls']")