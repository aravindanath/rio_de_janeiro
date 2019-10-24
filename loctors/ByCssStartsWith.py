import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.google.com")

# Css ^(caret symbol) --> Startswith
op.driver.find_element_by_css_selector("input[class^='gLF']").send_keys("Goa")

time.sleep(2)
op.driver.quit()