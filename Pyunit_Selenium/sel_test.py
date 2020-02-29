from selenium import webdriver
from pytest import fixtures


driver = webdriver.Chrome(executable_path='WebDriver/chromedriver_235')

driver.get('https://www.bseindia.com')
