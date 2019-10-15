from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

"""
https://github.com/SergeyPirogov/webdriver_manager

"""


driver = webdriver.Firefox(GeckoDriverManager().install())
driver.get("https://www.amazon.com")