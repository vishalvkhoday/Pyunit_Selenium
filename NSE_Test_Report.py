'''
Created on Jan 17, 2019

@author: vkhoday
'''
import unittest
from openpyxl import load_workbook
import HtmlTestRunner
from HtmlTestRunner.result import TestResult
import time
import logging
import os
import HTMLTestRunner
from Test_3 import login
import Test_3 
from selenium.webdriver.common.keys import Keys
import selenium


File_name = 'C:/Users/vkhoday/git/Selenium_NSE_Algo/Additonal_Utility/NSE_Script_codes.xlsx'
W_Sheet ='Sheet1'
driver= Test_3.driver
direct = os.getcwd()

results=unittest.TestResult()



class TestNseDataExt(unittest.TestCase):
    @classmethod
    def setUp(self):
        login()
        logging.info('Setup function successfully executed')
#         unittest.TestResult.addSuccess(self,"Login successfully")
        HTMLTestRunner.TestResult.addSuccess(self,"Login Successfull!!!")
        HtmlTestRunner.result.TestResult.addSuccess(self,"Login Successful")
        time.sleep(1)
        pass
    
    
    def testName1(self):
        rno = 1
        scrpt_Stus = Test_3.GetScriptName(File_name, W_Sheet)                    
        for scr_nm ,sts in scrpt_Stus.items():
            rno+=1
            results.startTestRun()
            print (scr_nm,sts)
            if sts =='Yes':
#                 TestNseDataExt.test_case_execute(self, scr_nm)
                Test_3.Result_gen(self)
        print('List complete')
#                 TestResult.wasSuccessful(self)
                
#                 TestNseDataExt.test_case_execute(self, scr_nm)

                
#     test=TestNseDataExt('testName1')           
#                 HtmlTestRunner.runner.HTMLTestRunner.run(self,TestNseDataExt.test_case_execute(self, scr_nm) )
#                 TestNseDataExt.test_case_execute(self, scr_nm)
#     @classmethod
#     def test_case_execute(self,scr_nm):
#         try:
# #             login()
#             driver.find_element_by_xpath('//*[@class="search"]/input[@id="keyword"]').send_keys(Keys.CLEAR)
#             driver.find_element_by_xpath('//*[@class="search"]/input[@id="keyword"]').send_keys(str(scr_nm).strip())
#             driver.set_page_load_timeout(4)
# #             driver.find_elements_by_xpath('//*[@class="search"]/input[@id="keyword"]').send_keys(Keys.ENTER)
#             driver.implicitly_wait(2)
#             pass
#         except:
#             print('Unknow error')
 
    def tearDown(self):
        logging.info("tear down method executed...")
        driver.quit()
        Wb =Test_3.ObjWorkBook(File_name)
        Wb.close()
        pass
    
 
        
if __name__ == "__main__":
    pass
    #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main(testrunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/Reports'))
    
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/Reports'))
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Pyunit_Selenium/Reports'))  
    
# Wb =Test_3.ObjWorkBook(File_name)
# Wb.close()             
    