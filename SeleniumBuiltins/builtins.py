import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys
op.driver.get("https://www.google.com")
# Fullscreen
op.driver.fullscreen_window()
op.driver.find_element_by_name('q').send_keys("Selenium Jobs",Keys.ENTER)
time.sleep(2)
# Navigating back
op.driver.back()
time.sleep(2)
# Navigating forward
op.driver.forward()
time.sleep(1)
# refreshing the page
op.driver.refresh()
# Getting the current URl
print(op.driver.current_url)
# Getting the page title
page = op.driver.title
print("Title: "+ page)
time.sleep(2)
# TO get the page source
print(op.driver.page_source)
# Quting /closing the browser
op.driver.quit()