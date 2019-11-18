from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.amazon.com"
        path = "../driver/chromedriver"
        driver = webdriver.Chrome(executable_path=path)
        driver.fullscreen_window()
        driver.get(baseUrl)
        driver.implicitly_wait(30)

        loginLink = driver.find_element(By.XPATH, "//span[text()='Hello, Sign in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

ff = ImplicitWaitDemo()
ff.test()