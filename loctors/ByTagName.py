import loctors.chromebrowser as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")

links = op.driver.find_elements_by_tag_name("a")

print("Total no of links:", len(links))

x = 1
for lnk in links:

    print(str(x)+" "+lnk.text +"--->"+lnk.get_attribute("href"))
    x=x+1

op.driver.quit()
