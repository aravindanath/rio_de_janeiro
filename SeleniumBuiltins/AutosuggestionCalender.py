import loctors.chromebrowser as op
from selenium.webdriver.common.by import By

import time


op.driver.get("https://www.redbus.in/")

op.driver.find_element_by_xpath("//*[@id='src']").send_keys("Goa")
list = op.driver.find_elements(By.XPATH, "//ul[@class='autoFill']")

city =  "South Goa"

for pickList in list:
    print(pickList.text)
    op.driver.find_element_by_xpath("//ul[@class='autoFill']/li[contains(text(),'"+city+"')]").click()

time.sleep(2)

op.driver.find_element_by_xpath("//*[@id='dest']").send_keys("Bang")
listDest = op.driver.find_elements(By.XPATH,"//ul[@class='autoFill']/li")

dropCity = "Madiwala, Bangalore"
for drop in listDest:
    print(drop.text)
    op.driver.find_element_by_xpath("//ul[@class='autoFill']/li[contains(text(),'" + dropCity + "')]").click()


time.sleep(2)

op.driver.find_element_by_xpath("//*[@id='search']/div/div[3]/span").click()

time.sleep(1)
onWard = op.driver.find_elements(By.XPATH,"//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")

for onWardDt in onWard:
    if onWardDt.text == "22":
        onWardDt.click()


op.driver.find_element_by_xpath("//*[@id='search']/div/div[4]/span").click()
time.sleep(1)
returndate = op.driver.find_elements(By.XPATH,"//div[@id='rb-calendar_return_cal']/table/tbody/tr/td")

for rtnDate in returndate:
    if rtnDate.text == "29":
        rtnDate.click()

time.sleep(2)
op.driver.find_element(By.XPATH,"//*[@id='search_btn']").click()

time.sleep(2)
op.driver.quit()