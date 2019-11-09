import loctors.chromebrowser as op

import time


op.driver.get("https://www.canarabank.in/")

title = op.driver.title
print("First window",title)

win1 = op.driver.current_window_handle

print("First window",win1)

op.driver.find_element_by_xpath("(//button[@type='submit'])[1]").click()

win2 = op.driver.window_handles

for handle in win2:
    op.driver.switch_to.window(handle)

print(op.driver.title)
second = op.driver.current_window_handle
print("Second window is " + str(second))

time.sleep(3)
op.driver.close()
time.sleep(1)
op.driver.switch_to.window(win1)
time.sleep(1)
op.driver.find_element_by_xpath("(//button[@type='submit'])[1]").click()
time.sleep(3)
op.driver.quit()