
import loctors.chromebrowser as op
import time

op.driver.get("https://www.amazon.com")
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone")

time.sleep(2)
op.driver.quit()

