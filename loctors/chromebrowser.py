from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
# ops.add_argument("--headless")

driver =  webdriver.Chrome(executable_path="../driver/chromedriver",options=ops)