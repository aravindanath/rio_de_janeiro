import loctors.chromebrowser as op

import time


op.driver.get("https://docs.oracle.com/javase/8/docs/api/")

op.driver.switch_to.frame("packageListFrame")

op.driver.find_element_by_link_text("java.applet").click()
time.sleep(2)

op.driver.switch_to.default_content()
op.driver.switch_to.frame("packageFrame")
op.driver.find_element_by_link_text("AppletContext").click()
time.sleep(1)

op.driver.switch_to.default_content()
op.driver.switch_to.frame("classFrame")

t = op.driver.find_element_by_xpath("//h2[@class='title']").text
print(t)

op.driver.quit()