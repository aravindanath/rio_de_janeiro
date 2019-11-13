import loctors.chromebrowser as op


import time
"""
https://www.w3schools.com/jsref/met_win_scrollto.asp
"""


op.driver.get("https://www.amazon.com")
op.driver.fullscreen_window()
time.sleep(2)

ele = op.driver.find_element_by_xpath("//*[text()='Back to top']")
# Scroll to perticular ele
op.driver.execute_script("arguments[0].style.border = '3px solid Red'", ele)

op.driver.execute_script("arguments[0].scrollIntoView();",ele)



time.sleep(2)

ele.click()

time.sleep(2)
op.driver.quit()