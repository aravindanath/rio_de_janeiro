import loctors.chromebrowser as op
from selenium.webdriver.common.action_chains import ActionChains

import time


op.driver.get("http://demo.guru99.com/test/drag_drop.html")
op.driver.fullscreen_window()

time.sleep(2)
src1 = op.driver.find_element_by_xpath("//*[@id='fourth']/a")
dct1 = op.driver.find_element_by_xpath("//*[@id='amt7']/li")


src2 = op.driver.find_element_by_xpath("//*[@id='credit1']/a")
src3 = op.driver.find_element_by_xpath("//*[@id='credit2']/a")

dct3 = op.driver.find_element_by_xpath("//*[@id='bank']/li")
dct4 = op.driver.find_element_by_xpath("//*[@id='loan']/li")


act = ActionChains(op.driver)
time.sleep(2)
act.drag_and_drop(src1,dct1).perform()



time.sleep(2)
# op.driver.quit()
