"""
https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
https://peter.sh/experiments/chromium-command-line-switches/#headless
"""

from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
# ops.add_argument("--headless")
ops.add_argument("--incognito")

path = "../driver/chromedriver"
driver = webdriver.Chrome(options=ops,executable_path=path)

driver.get("https://www.facebook.com")
print(driver.title)

driver.quit()



