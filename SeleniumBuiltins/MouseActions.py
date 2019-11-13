import loctors.chromebrowser as op
from selenium.webdriver.common.action_chains import ActionChains

import time


op.driver.get("https://www.hdfcbank.com/")
op.driver.fullscreen_window()

try:
    op.driver.find_element_by_xpath("//img[@class='popupCloseButton']").click()
except:
    print("Pop up not appeared")

invest = op.driver.find_element_by_xpath("//*[text()='INVEST']")
knowledge = op.driver.find_element_by_xpath("//*[text()='Knowledge Center']")

act = ActionChains(op.driver)
# Mouse hover
act.move_to_element(invest).perform()
time.sleep(2)
act.click(knowledge).perform()




time.sleep(2)
op.driver.quit()
