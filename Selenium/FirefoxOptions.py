
path = "../driver/geckodriver"

from selenium import  webdriver
from selenium.webdriver.firefox.options import Options

ops = Options()
# TO diabale notification
ops.set_preference("dom.webnotifications.enabled", False)
ops.set_preference("dom.push.enabled", False)
ops.add_argument("-private")

driver = webdriver.Firefox(executable_path=path,options=ops)


driver.get("https://www.icicibank.com/")


driver.find_element_by_xpath("//*[@class='pl-login-ornage-box']").click()


"""
For Windows:

path  = "D:\\driver\\geckodriver.exe"

"""

driver.quit()



