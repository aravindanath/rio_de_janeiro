import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class examplePython(unittest.TestCase):
    dc = {}
    testName = 'Quick Start Chrome Browser Demo on cloud'
    driver = None

    def setUp(self):
        self.dc['testName'] = self.testName
        self.dc['browserName'] = "chrome"
        self.dc['browserVersion'] = ""
        self.dc['platform'] = ""
        self.dc['accessKey'] = "8crRVS6W13ABOJVGkLj9oQXVWPKBqOxakgKX_ECqC50"
        self.driver = webdriver.Remote('https://cloud.seetest.io/wd/hub', self.dc)

    def testExperitest(self):
        for x in range(0, 20):
            self.driver.get("http://www.google.com")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, 'q')))
            searchBar = self.driver.find_element_by_name('q')
            searchBar.click()
            searchBar.send_keys('Aravindanath')
            searchBar.send_keys(Keys.ENTER)

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()
