import loctors.chromebrowser as op
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


op.driver.get("https://www.wikipedia.org/")

lang = op.driver.find_element_by_xpath("//select[@id='searchLanguage']")
time.sleep(2)

sle = Select(lang)
sle.select_by_index(10)


time.sleep(2)

sle.select_by_value("hy")

time.sleep(2)


sle.select_by_visible_text("हिन्दी")

time.sleep(2)
op.driver.quit()