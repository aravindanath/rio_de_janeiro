import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys

testData={"url":"https://www.google.com","Search":"selenium python jobs in bangalore for 5 yrs exp"}


op.driver.get(testData["url"])
time.sleep(2)
op.driver.find_element_by_name("q").send_keys(testData["Search"],Keys.ENTER)
time.sleep(3)
op.driver.quit()