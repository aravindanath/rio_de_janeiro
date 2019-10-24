import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.google.com")

op.driver.find_element_by_css_selector("input[name='q']").send_keys("selenium jobs")

time.sleep(2)
op.driver.quit()