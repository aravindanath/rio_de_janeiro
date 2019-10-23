import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("http://the-internet.herokuapp.com/tables")

name = "//table[@id='table1']/tbody/tr/td[contains(text(),'NAME')]//following::td[3]".replace("NAME","Jason")
web = op.driver.find_element_by_xpath(name).text

print(web)

time.sleep(2)
op.driver.quit()