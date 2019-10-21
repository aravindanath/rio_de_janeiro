import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.facebook.com")

var = op.driver.find_element_by_xpath("//label[contains(text(),'Email')]").text
print(var)

assert var == "Email or Phone"


time.sleep(2)
op.driver.find_element_by_xpath("//input[contains(@id,'em')]").send_keys("arvind@email.com")

time.sleep(2)
op.driver.find_element_by_xpath("//input[contains(@id,'pa')]").send_keys("876sdfgh")


time.sleep(2)
title = op.driver.find_element_by_xpath("//span[text()='Create an account']").text
print(title)
time.sleep(2)
op.driver.quit()

#