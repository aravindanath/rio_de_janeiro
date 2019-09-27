

# city = "Banglore"
# #
# # assert city == "Bangalore"


import browser.openChrome as op

op.driver.get("https://www.google.com")

pageTitle = op.driver.title

print(pageTitle)
#     actual  === excepted
assert pageTitle == "Facebook"

op.driver.quit()