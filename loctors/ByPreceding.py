import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("http://the-internet.herokuapp.com/tables")

name = "//table[@id='table1']/tbody/tr/td[contains(text(),'AMT')]//preceding::td[3]".replace("AMT","$51.00")
web = op.driver.find_element_by_xpath(name).text

print(web)

time.sleep(2)
op.driver.quit()