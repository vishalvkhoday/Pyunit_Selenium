'''
Created on Sep 5, 2020

@author: DELL
'''
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


def getRemoteBrowser():
    Options = ChromeOptions()
    Options.add_argument("start-maximized")
    Options.add_argument("headless")
    Options.add_argument("disable-infobar")
    BrwChrome =Chrome(executable_path="C:/Users/DELL/git/Selenium_NSE_Algo/Additonal_Utility/chromedriver", chrome_options=Options)
    hubURL="http://192.168.1.102:4444/wd/hub"
    rmtDriver = webdriver.Remote(command_executor=f"http://localhost:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME,  options=Options)
    return rmtDriver
    
Driver =getRemoteBrowser()
Driver.get("https://www.bseindia.com/")
# Driver.get_screenshot_as_png()
print(Driver.title)
print("Done")


