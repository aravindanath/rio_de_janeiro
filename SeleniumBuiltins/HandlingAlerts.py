import loctors.chromebrowser as op

class HandlingAletsUsingSelenium():


    def alertAccept(self):

        op.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

        op.driver.find_element_by_xpath("//input[@type='submit']").click()

