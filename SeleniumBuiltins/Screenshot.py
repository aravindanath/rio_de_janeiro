import loctors.chromebrowser as op



op.driver.get("https://www.amazon.com")


op.driver.get_screenshot_as_file("/Users/aravindanathdm/Documents/rio_de_janeiro/ScreenShot/demo.png")

op.driver.quit()