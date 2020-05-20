import time
from GeneralStoreAppAutomation import BaseFile_AppLaunch as bs
from GeneralStoreAppAutomation import GenericFile as gf
'''
This code is for Toast message handling (It's kind of an error where you don't enter name and click ok to continue)
'''

time.sleep(2)
# clicking on dropdown
bs.driver.find_element_by_id("spinnerCountry").click()
# below code is for scrolling
gf.scroll_and_click("Aruba", bs.driver)
time.sleep(2)
bs.driver.find_element_by_id("com.androidsample.generalstore:id/radioFemale").click()
bs.driver.find_element_by_id("com.androidsample.generalstore:id/btnLetsShop").click()
msg = bs.driver.find_element_by_xpath("//android.widget.Toast[@text='Please enter your name']")
assert msg.text == "Please enter your name"
gf.takeScreenshot(bs.driver, "../toast_message.png")
print("Screenshot captured successfully for Toast Message")