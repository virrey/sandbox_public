import pandas as pd
import numpy as np
import os,sys
import time
import re
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class Scraper:
    """
    Scraper class in ariScrape.py used to create a scraper object that
    uses chromedriver to open a url and try to find an xpath to extract
    value from. You can set the property 'self.url' directly before
    LoadPage or you can send in a list of url parts, if you are iterating
    through xpaths, with the setXPathFromParts method.
    """
    def __init__(self):
        '''
        Sets up the chromedriver for either darwin (mac) or win32 (windows).
        '''
        self.verbose = False
        self.platform = sys.platform # 'darwin' is mac 'win32' is windows
        self.driverpath = ""
        self.driver = None
        self.xpath = ""
        self.url = ""
        self.xpath_pattern = []
        self.url_pattern = []
        self.sleepMin, self.sleepMax = 3,10
        self.sleep = 3
        self.scrapped_item = None
        
    def getChromeDriverPath(self, pth='/Applications/chromedriver'):
        '''
        Points to chromedriver path or as defined by user.
        Check platform 'darwin' (mac) or 'win32' (win).
        '''
        if pth == '/Applications/chromedriver':
            p = self.platform
            if p == 'win32':
                self.driverpath = r'C:\webdriver\chromedriver.exe'
            elif p == 'darwin':
                self.driverpath = '/Applications/chromedriver'
        else:
            self.driverpath = pth # user-def path assignment

    def getChromeDriver(self):
        '''
        Initialize chromedriver. If this failed check your driverpath.
        On macs it's looking for the driver in /Applications/chromedriver
        On win it's looking in C:\webdriver\chromedriver.exe
        I'll update getChromeDriverPath later to allow user def path.
        '''
        os.environ['webdriver.chrome.driver'] = self.driverpath
        self.driver = webdriver.Chrome(self.driverpath)
    
    def setURLFromParts(self, url_parts):
        self.url = ''.join([str(p) for p in url_parts])
    
    def setXPathFromParts(self, xpath_parts):
        self.xpath = ''.join([str(p) for p in xpath_parts])
            
    def LoadPage(self):
        '''
        Loads url provided either via self.url directly or via
        url created from setURLFromParts (if you're looping
        through urls and changing string elements.)
        '''
        self.driver.set_page_load_timeout(15)
        try:
            if self.verbose: print('Try to get url:',self.url)
            self.driver.get(self.url)
        except TimeoutException:
            if self.verbose: print('Stop Loading Page Sent')
            self.driver.execute_script('window.stop()')
        except TimeoutError:
            if self.verbose: print('Timeout Error... Moving Next...')
            self.driver.execute_script('window.stop()')
        return

    def RandSleep(self):
        '''
        This function is ultimately for cycling through random
        values of time to sleep in between LoadPages.
        '''
        self.sleep = np.random.randint(self.sleepMin,self.sleepMax)
        
    def ExtractFloatAtXPath(self):
        '''
        Used to extract a float at xpath, and re.sub some
        weird characters out.
        '''
        try:
            if self.verbose: print('Try finding element at:',self.xpath)
            val = self.driver.find_element_by_xpath(self.xpath).text
        except:
            if self.verbose: print('excepted')
            val = 0.0
        else:
            if self.verbose: print('XPath Found at',self.xpath)
            if val in ['N/A','n/a','N/a','0','']:
                val = '0.0'
            val = float(re.sub('[()]','-',re.sub(r"[$%,\)]", "", val)))
        self.scrapped_item = val
        if self.verbose: print("Item retrieved:",str(self.scrapped_item))