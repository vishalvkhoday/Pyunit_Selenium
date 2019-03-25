'''
Created on Feb 21, 2019

@author: vkhoday
'''
import unittest
import HTMLTestRunner
import HtmlTestRunner
from Test_3 import *


class Test5(unittest.TestCase):

    @classmethod
    def setUp(self):
        login()
        driver.set_page_load_timeout(4)
        pass


    

    @classmethod
    def testNseValid(self):
        for i in range(1,5):
            Script_input()
        print (i)
        pass
    @classmethod
    def testBseValid(self):
        @HtmlTestRunner.runner.HTMLTestRunner.start_time
        def loopname1(self):
            for i in range(1,5):
                Script_input()
                print (i)
        
        pass
        

    def tearDown(self):
        broswer_close()
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output='C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/Reports'))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vkhoday/eclipse-workspace/Pyunit_Selenium/Reports'))
    