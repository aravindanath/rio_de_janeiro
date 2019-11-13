import loctors.chromebrowser as op

import time


op.driver.get("https://www.wikipedia.org/")

lang =  op.driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")

print("Total no of lang: ",len(lang))
emptyLang = []
for lg in lang:
    # print(lg.text)
    emptyLang.append(lg.text)


print("Un sorted",emptyLang)
emptyLang.sort()
print("Sorted",emptyLang)

op.driver.quit()