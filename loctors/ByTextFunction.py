import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.facebook.com")

title= op.driver.find_element_by_xpath("//div[text()='Facebook helps you connect and share with the people in your life.']").text
print(title)
time.sleep(2)

t1 = op.driver.find_element_by_xpath("//div[contains(text(),'quick')]").text
print(t1)
op.driver.quit()