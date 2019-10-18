import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.icicibank.com/")
time.sleep(2)
op.driver.find_element_by_class_name("pl-login-ornage-box").click()
time.sleep(1)
op.driver.quit()