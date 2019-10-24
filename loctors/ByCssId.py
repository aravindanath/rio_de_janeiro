import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys



op.driver.get("https://www.amazon.com")

# Css ID --> # //input[@id=twotabsearchtextbox] // twotabsearchtextbox //#twotabsearchtextbox
op.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Samsung smart watch")



time.sleep(2)
op.driver.quit()