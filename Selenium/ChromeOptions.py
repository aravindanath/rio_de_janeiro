"""
https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
https://peter.sh/experiments/chromium-command-line-switches/#headless
"""

from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")


path = "../driver/chromedriver"
driver = webdriver.Chrome(options=ops,executable_path=path)

driver.get("https://icicibank.com")
driver.find_element_by_xpath("//*[@id='main']/div[2]/ul/li[9]/a/span").click()

