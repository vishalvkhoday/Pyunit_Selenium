'''
Created on Jan 28, 2019

@author: vkhoday
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import Command
from selenium.webdriver.common.by import By
from math import exp

# chrome_opt = webdriver.ChromeOptions()
# chrome_opt.add_argument("headless")
driver=webdriver.Chrome(executable_path='C:/Python36/chromedriver_235')
dropdown = '//*[@id="searchLanguage"]'
lst_lang = '//*[@id="searchLanguage"]'

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

elembt = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
ActionChains(driver).click_and_hold(elembt).perform()
ActionChains(driver).pause(2)
ActionChains(driver).release(elembt).perform()

# weelem =WebDriverWait.until(lambda x: x.find_element_by_id("searchLanguage").is_displayed())
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("searchLanguage"))
print(element)

# elemt = driver.find_element(By.TAG_NAME,'option')
# sel_Elem = Select(elemt)
# print(sel_Elem.all_selected_options)

selett = driver.find_element_by_xpath(dropdown)

# langlst = str(selett.text).splitlines()
# for lng in langlst:
#     print(str(lng).capitalize())

# selvvt = Select(selett)
# lang = selvvt.options

# for langval in lang:
#     print(langval)

driver.find_element_by_xpath(dropdown).click()
sleep(2)
driver.find_element_by_xpath(dropdown).send_keys(Keys.ARROW_DOWN)

driver.find_element_by_xpath(dropdown).send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath(dropdown).send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath(dropdown).send_keys(Keys.ENTER)
Select(driver.find_element_by_tag_name("select")).select_by_index(2)
# ActionChains(driver).context_click().perform()
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
ActionChains(driver).context_click(dropdown)
ActionChains(driver).pause(4).perform()
ActionChains(driver).send_keys_to_element(dropdown)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
ActionChains(driver).pause(4).perform()
sleep(5)
ActionChains(driver).key_down(Keys.DOWN)
selval = driver.find_element_by_xpath(dropdown)
try:
    sel = Select(selval)
    
    lan =sel.options
    for x,lan in enumerate(range(1,len(sel.options)),start=1):
        lanxpath = str('//*[@id="searchLanguage"]/option[') +str(lan)+str(']')
        lanText = driver.find_element_by_xpath(lanxpath).get_attribute('lang')
        print('{}) {}'.format(x,lanText))
        sel.select_by_index(x-1)
        sleep(2)
#     sel.select_by_visible_text('English')
    sel.select_by_value("de")
    sleep(5)

except WebDriverException:
    print('This is exception {}'.format(WebDriverException('Error on page',screen=None)))


