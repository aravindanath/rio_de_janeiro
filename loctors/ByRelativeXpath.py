import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")
#                                  //input[@name='q']
# //TAGNAME[@Attribute = 'VALUE']
op.driver.find_element_by_xpath("//input[@name='q']").send_keys("Selenium jobs",Keys.ENTER)

time.sleep(2)
op.driver.quit()

