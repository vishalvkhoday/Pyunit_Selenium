'''
Created on Dec 13, 2018

@author: vkhoday
'''

import unittest
import Repo_Object as obj_r
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import ScreenshotException
import logging
import time
import HtmlTestRunner

import sys
from HTMLTestRunner import _TestResult


# from selenium.webdriver.common.alert import Alert
# from allure_pytest.plugin import allure  

driver = obj_r.driver


class MoneyControl(unittest.TestCase):        
    
    results = unittest.TestResult()
    results.startTest('setUp')
    def setUp(self):
        unittest.TestCase.setUp(self)        
        driver.get(obj_r.url)
        logging.info("Launched browser")
        logging.critical('Title wrong')
        print(driver.get_log('browser'))
        
        driver.implicitly_wait(10)
        obj_r.Screenshot()
        obj_r.get_screenShot()
        obj_r.temp_scr_shot()
        
        try:
            driver.maximize_window()
            try:
                p_tile = driver.title

                assert p_tile.find("Stock/Share Market Investment") == 0
                
                
            except AssertionError:
                print ("Page title error")
            winHan = driver.window_handles
            
#             for i in range(0,len(winHan)):
#                 driver.switch_to_window(winHan[i])
            
            #driver.current_window_handle.send_key(Keys.LEFT_CONTROL +'t')
            driver.find_element_by_xpath(obj_r.home_scr_txt).send_keys(Keys.RETURN)
            alt_txt = driver.switch_to.alert.text
            print(alt_txt)
            
#             driver.switch_to.alert.accept()
            driver.switch_to.alert.dismiss()
            
            pass
            
        except:
            None
            
#         try:
#             driver.find_element_by_xpath(obj_r.home_link).click()
#             
#         except:
#             None
#             obj_r.Screenshot()
        
    
    def test_get_scriptList(self):
        str_scrname =dict(obj_r.get_Script_name())        
        for i in str_scrname:
            print (i)
            if str_scrname.get(i)== 'Yes':
                print(i)
                
                
                None

    
    def test_StockInfo(self,i):            
#             if str_scrname.get(i) == "Yes":                
            driver.find_element_by_xpath(obj_r.home_scr_txt).send_keys(i)
            driver.find_element_by_xpath(obj_r.home_scr_txt).send_keys(Keys.RETURN)
            time.sleep(5)
            driver.set_page_load_timeout(15)
            driver.implicitly_wait(10)
            print(driver.current_window_handle)
#                 driver.switch_to.window(driver.current_window_handle)
            
            driver.find_element_by_xpath(obj_r.home_scr_txt).click()
            driver.find_element_by_xpath(obj_r.home_scr_txt).send_keys(Keys.RETURN)
            time.sleep(2)
            alt_dialog = driver.switch_to.alert
            print(alt_dialog.text)
            alt_dialog.accept()
            handls =driver.window_handles
            siz = len(handls)
            for x in range(siz):
                driver.switch_to.window(handls[x])
                print(driver.title)
            
                
                
    pass
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)        
        driver.close()
    
    
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/Reports'))
    
    
    
    
    