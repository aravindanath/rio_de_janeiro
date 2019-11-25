import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.fullscreen_window()
op.driver.get("https://www.yatra.com/")
time.sleep(2)
src = op.driver.find_element_by_css_selector("#BE_flight_origin_city")
src.clear()
time.sleep(2)
src.send_keys("Bangalore",Keys.ENTER)
time.sleep(2)
arr = op.driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
arr.clear()
arr.send_keys("Chennai")
time.sleep(3)
airport = op.driver.find_elements_by_xpath("//div[@class='viewport']/div/div/li/div/p")
time.sleep(2)


city =op.driver.find_element_by_xpath("//div[@class='viewport']/div/div/li[@class='active ac_over']")
if city.is_displayed():
    city.click()


time.sleep(3)
op.driver.close()



