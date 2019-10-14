from selenium import webdriver
# path ="c:\\driver\\chromedriver.exe"
# path  = "c:\\driver\\geckodriver.exe --> window
path = "../driver/chromedriver"
browser = "chrome"

if browser == "ff":
    driver =  webdriver.Firefox(executable_path="../driver/geckodriver")
elif browser ==  "chrome":
    driver = webdriver.Chrome(executable_path=path)



driver.get("https://www.amazon.com")