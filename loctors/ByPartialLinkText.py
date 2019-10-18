import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")

op.driver.find_element_by_partial_link_text("Ima").click()
time.sleep(2)
op.driver.find_element_by_name("q").send_keys("Boston",Keys.ENTER)

time.sleep(3)
op.driver.quit()
