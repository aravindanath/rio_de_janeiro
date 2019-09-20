
from selenium import  webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
env =  "mac"

if  env is "win":
    path = "..//driver//chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path, options=ops)
    driver.fullscreen_window()
elif env is "mac":
    path = "..//driver//chromedriver"
    driver = webdriver.Chrome(executable_path=path, options=ops)
    driver.fullscreen_window()





