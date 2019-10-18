import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")
#                                  //input[@name='q']

op.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div/div/div/div[2]/input").send_keys("Selenium jobs",Keys.ENTER)

time.sleep(2)
op.driver.quit()

