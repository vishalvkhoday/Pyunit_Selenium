'''
Created on Feb 21, 2019

@author: vkhoday
'''
from selenium import webdriver
import unittest
import sys
from xmlrunner import *


class Grid2(unittest.TestCase):   
    capabilities = None
   
    def setUp(self):       
        self.driver = webdriver.Remote(desired_capabilities={           
            "node":port,
            "platform":platform,
            "browserName":browser
        })
        print ("set up executed")
       
   
    def test_example(self):
        self.driver.get("http://www.google.com")
        print ("open google url")
        self.assertEqual(self.driver.title, "Google")
        print ("verify title")
        self.driver.find_element_by_id("gbqfq").clear()
        self.driver.find_element_by_id("gbqfq").send_keys("testing")
        print ("enter text in serach field")
        self.driver.find_element_by_id("gbqfb").click()
        print ("click on search button")   

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":    
    args = sys.argv   
    port  = args[1]
    platform  = args[2]
    browser = args[3]
    suite = unittest.TestSuite()
    suite.addTest(Grid2('test_example'))
    runner = XMLTestRunner('c:/results_ExampleTestCase_%s.xml' % (browser), "w")
#     runner = XMLTestRunner(file('c:/results_ExampleTestCase_%s.xml' % (browser), "w"))
    runner.run(suite)