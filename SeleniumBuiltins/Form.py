import loctors.chromebrowser as op


import time


op.driver.get("https://www.toolsqa.com/automation-practice-form/")
op.driver.fullscreen_window()

op.driver.find_element_by_xpath("//input[@name ='firstname']").send_keys("Deepak")
time.sleep(1)
op.driver.find_element_by_xpath("//input[@value ='Male' and @id='sex-0']").click()
op.driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)
op.driver.find_element_by_xpath("//*[@id='exp-2']").click()
time.sleep(2)
op.driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("01/11/2019")
time.sleep(2)
op.driver.execute_script("window.scrollBy(0,200)","")
cb =  op.driver.find_elements_by_xpath("//*[@type='checkbox']")
for cBox in cb:
    cBox.click()

up = op.driver.find_element_by_xpath("//*[@id='photo']")
up.send_keys("/Users/aravindanathdm/Desktop/demo.png")

time.sleep(2)

op.driver.find_element_by_xpath("//*[text()='Test File to Download']").click()
time.sleep(4)
op.driver.quit()
