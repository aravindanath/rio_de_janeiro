
import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.icicibank.com/")

# css class is identified by .

op.driver.find_element_by_css_selector(".pl-login-ornage-box").click()


op.driver.quit()