from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://www.google.com/")
title=  driver.title
driver.save_screenshot("test.png")
driver.get_screenshot_as_png();
print("Page Title "+title)
driver.quit()
