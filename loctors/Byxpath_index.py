import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.hdfcbank.com/")

time.sleep(2)

try:
    op.driver.find_element_by_xpath("//img[@class='popupCloseButton']").click()
except:
    print("popup handled")

op.driver.find_element_by_xpath("//div[@id='custom-button'][1]/button[@class='btn btn-primary login-btn ng-scope']").click()

time.sleep(2)


op.driver.get("https://www.facebook.com")

time.sleep(2)
op.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("5678909876")

time.sleep(2)
op.driver.quit()

#