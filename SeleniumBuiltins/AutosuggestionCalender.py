import loctors.chromebrowser as op

import time


op.driver.get("https://www.redbus.in/")


op.driver.find_element_by_css_selector("#src").send_keys("Bang")

src = op.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")

for li in src:
    print(len(li))
    print(li.text)


time.sleep(2)

op.driver.quit()