'''
Created on Mar 15, 2019

@author: vkhoday
'''

 
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import  ElementNotVisibleException
import time
 
 
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=options,executable_path="WebDriver/chromedriver_235", service_args=["--verbose", "--log-path=WebDriver/qc1.log","w+"])
actions = ActionChains(driver)
 
driver.get("https://www.google.com")
driver.implicitly_wait(10)
driver.maximize_window()
winHanl = driver.window_handles
xpath_scrtxt = '//*[@id="form_topsearch"]/input[@id="search_str"]'
# xpath_scrtxt = '//*[@id="form_topsearch"]/input[@id="search_str"]'
for win in winHanl:
    driver.switch_to_window(win)
    driver.execute_script("window.open('https://www.moneycontrol.com')")
    WebDriverWait(driver,15).until(EC.visibility_of_all_elements_located)
    driver.find_element_by_id("search_str").click()
    actions.key_down(Keys.ENTER).perform()
    WebDriverWait(driver, 10).until(EC.alert_is_present)
#     driver.find_element(By.XPATH,'').send_keys(Keys.COMMAND + 't')
#     driver.current_window_handle
    
driver.implicitly_wait(10)
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
WebDriverWait(driver, 10).until(EC.alert_is_present)
time.sleep(5)

# 
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 
# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'WebDriver/chromedriver_235')
# driver.get("http://www.google.co.in")
# print("Initial Page Title is : %s" %driver.title)
# windows_before  = driver.current_window_handle
# print("First Window Handle is : %s" %windows_before)
# driver.execute_script("window.open('https://www.yahoo.com')")
# WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
# windows_after = driver.window_handles
# new_window = [x for x in windows_after if x != windows_before][0]
# driver.switch_to_window(new_window)
# print("Page Title after Tab Switching is : %s" %driver.title)
# print("Second Window Handle is : %s" %new_window)