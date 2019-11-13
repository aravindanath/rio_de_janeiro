import loctors.chromebrowser as op
from selenium.webdriver.common.action_chains import ActionChains

import time


op.driver.get("https://demoqa.com/droppable/")
op.driver.fullscreen_window()
time.sleep(2)
src1 = op.driver.find_element_by_xpath("//*[@id='draggable']")
dct1 = op.driver.find_element_by_xpath("//*[@id='droppable']")

act = ActionChains(op.driver)
act.drag_and_drop(src1,dct1).perform()

time.sleep(2)
op.driver.quit()
