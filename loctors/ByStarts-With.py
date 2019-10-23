import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")

op.driver.find_element_by_xpath("//input[starts-with(@class,'gLF')]").send_keys("Weather in Goa",Keys.ENTER)

time.sleep(2)
op.driver.quit()