import loctors.chromebrowser as op

import time

class HandlingAletsUsingSelenium():


    def alertAccept(self):

        op.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        op.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(1)
        alert =  op.driver.switch_to.alert
        # Accept will click on OK button
        alert.accept()
        time.sleep(1)
        op.driver.find_element_by_id("login1").send_keys("deepak@gmail.com")

    def alertDismiss(self):

        op.driver.get("http://the-internet.herokuapp.com/javascript_alerts")
        op.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
        alert = op.driver.switch_to.alert
        alert.accept()
        result = op.driver.find_element_by_xpath("//*[contains(text(),'You clicked: Ok') or contains(text(),'You clicked: Cancel')]").text
        print(result)

    def alertSendKeys(self):
        op.driver.get("http://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(1)
        ele = op.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
        ele.click()
        time.sleep(1)
        alert = op.driver.switch_to.alert
        alert.send_keys("Hello guys")
        time.sleep(2)
        alert.accept()
        time.sleep(1)
        val = op.driver.find_element_by_xpath("//p[@id='result']").text
        print(val)

        # assert val == "Hello guys"




    def close(self):
        op.driver.quit()

c=  HandlingAletsUsingSelenium()
# c.alertAccept()
# c.alertDismiss()
c.alertSendKeys()
c.close()
