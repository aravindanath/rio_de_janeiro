import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys


op.driver.get("https://www.google.com")

op.driver.find_element_by_name("q").send_keys("Selenium jobs in bangalore",Keys.ENTER)

time.sleep(2)
op.driver.quit()