import browser.openChrome as op


op.driver.get("https://www.wikipedia.org/")

lang = op.driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")


print("Total no of lang", len(lang))

empty =[]

print("List", empty)

for li in lang:

    empty.append(li.text)

print("Normal List", empty)
empty.sort()
print("SOrted List", empty)

op.driver.quit()