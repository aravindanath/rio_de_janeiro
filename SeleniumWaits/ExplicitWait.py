from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
# https://selenium-python.readthedocs.io/waits.html



class ExplicitWait():


    def setup(self):
        path = "../driver/geckodriver"
        driver = Firefox(executable_path=path)
        driver.fullscreen_window()
        driver.get("https://www.expedia.com/")
        # driver.implicitly_wait(.5)
        driver.find_element_by_id("tab-flight-tab-hp").click()
        driver.find_element_by_xpath("(//span[text()='Flying from']//following::input[1])[1]").send_keys("Bengaluru, India (BLR-Kempegowda Intl.)")

        driver.find_element_by_xpath("(//span[text()='Flying to']//following::input[1])[1]").send_keys("Boston",Keys.ENTER)

        driver.find_element_by_xpath("(//span[text()='Departing']//following::input[2])[1]").send_keys("10/12/2019")

        # driver.find_element_by_xpath("(//span[text()='Departing']//following::input[2])[2]").send_keys("11/01/2020")



        driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


        





        wait = WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])

        element =wait.until(ec.element_to_be_clickable((By.XPATH,"(//button[@type='button'])[34]")))

        element.click()









        # driver.quit()


i =ExplicitWait()
i.setup()