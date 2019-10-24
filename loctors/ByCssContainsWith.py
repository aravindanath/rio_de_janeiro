import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.google.com")

# Css * --> Startswith
op.driver.find_element_by_css_selector("input[class*='fi']").send_keys("Goa weather", Keys.ENTER)

time.sleep(2)
op.driver.quit()