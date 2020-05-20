import time
from GeneralStoreAppAutomation import BaseFile_AppLaunch as bs
from GeneralStoreAppAutomation import GenericFile as gf

time.sleep(2)
# clicking on dropdown
bs.driver.find_element_by_id("spinnerCountry").click()
# below code is for scrolling
city = "Bahrain"
gf.scroll(city, bs.driver)
bs.driver.find_element_by_xpath("//*[@text='"+city+"']").click()
#bs.driver.find_element_by_class_name("android.widget.EditText").send_keys("Lakshmi")
bs.driver.find_element_by_id("com.androidsample.generalstore:id/nameField").click()

bs.driver.press_keycode(36)
# use 1 as extra key-code for capital letter
bs.driver.press_keycode(29, 1)
bs.driver.press_keycode(46, 1)
bs.driver.press_keycode(37, 1)


'''name_list = [36, 29, 46, 37]
for name in name_list:
    gf.use_keyboard(bs.driver, name)
    time.sleep(2)'''
bs.driver.find_element_by_xpath("//*[@class='android.widget.RadioButton' and @text='Female']").click()
gf.hidekeyboard(bs.driver)
time.sleep(2)
'''bs.driver.find_element_by_id("btnLetsShop").click()
time.sleep(3)
gf.takeScreenshot(bs.driver, "../demo.png")
print("Captured screenshot")
gf.scroll("Jordan Lift Off", bs.driver)
products = bs.driver.find_elements_by_id("com.androidsample.generalstore:id/productName")
print("Total No.of products are : ", len(products))
for i in products:
    tp = i.text
    if tp == "Jordan Lift Off":
        cart_add = bs.driver.find_elements_by_xpath("//*[@text='ADD TO CART']")
        cart_add[1].click()

print("Desired product added to cart")
time.sleep(2)
bs.driver.find_element_by_id("appbar_btn_cart").click()
time.sleep(2)
tc = bs.driver.find_element_by_xpath("//*[@text='Please read our terms of conditions']")
gf.longpress(bs.driver, tc)
gf.takeScreenshot(bs.driver, "../demo2.png")
bs.driver.close_app()
print("App closed successfully")



'''