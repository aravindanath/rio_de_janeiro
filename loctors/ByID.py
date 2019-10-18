
import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.amazon.com")
# op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone",Keys.ENTER)

search = op.driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("iphone")
time.sleep(1)
search.clear()
search.send_keys("Samsung",Keys.ENTER)


time.sleep(2)
op.driver.quit()

