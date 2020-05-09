'''
Created on Mar 15, 2019

@author: vkhoday
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time
x=1
try:
    assert x<0
except AssertionError as AE:
    print(AE.args)
xpath_footer ='//*[@id="quicklinkdiv"]'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")

driver = webdriver.Chrome(chrome_options=options,executable_path='WebDriver/chromedriver_235')
Actions = ActionChains(driver)
driver.get('https://www.bseindia.com')
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath_footer)))
main_win = driver.window_handles
Elem_footer=driver.find_element_by_xpath(xpath_footer)
print (Elem_footer.parent)
Elem_footer.location_once_scrolled_into_view
loc_x,loc_y =Elem_footer.location.values()
link_lst = Elem_footer.get_attribute("innerText").splitlines()
for xx,link in enumerate(link_lst,start=1):
    try:    
        link_element =driver.find_element_by_link_text(link)
        ActionChains(driver).key_down(Keys.CONTROL).click(link_element).key_up(Keys.CONTROL).perform()
        time.sleep(3)
        win_list = driver.window_handles
        driver.switch_to.window(win_list[xx])
        time.sleep(3)
        driver.switch_to.window(main_win[0])
        WebDriverWait(driver,10).until(EC.new_window_is_opened)
#         driver.execute_script("window.open(www.bseindia.com)")
    except Exception as e:
        print(e.args,"\n","****-----"*14)
        
time.sleep(4)