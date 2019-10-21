import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.facebook.com")

var = op.driver.find_element_by_xpath("//input[@type='password' and @name='reg_passwd__']").send_keys("675432")



count =  op.driver.find_elements_by_xpath("//input[@name='reg_passwd__' or @type='password']")

print("No of password fields: "+str(len(count)))
time.sleep(2)
op.driver.quit()

#