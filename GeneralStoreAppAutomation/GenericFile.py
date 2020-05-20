import subprocess
import time
from appium.webdriver.common.touch_action import TouchAction
global driver
from appium import webdriver
#x = subprocess.call("adb devices")

def scroll(text, driver):
    automatorString = 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().textContains("' + text + '"));'
    driver.find_elements_by_android_uiautomator(automatorString)
    return driver

def scroll_and_click(text, driver):
    automatorString = 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().textContains("' + text + '"));'
    driver.find_elements_by_android_uiautomator(automatorString)
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + text + "']").click()
    return driver

def takeScreenshot(driver, path):
    driver.save_screenshot(path)
    return driver

def tap(driver, element):
    actions = TouchAction(driver)
    actions.tap(element)
    actions.perform()
    return driver

'''def capture_screenshot(driver, path):
    timeStamp = time.strftime("%Y_%m_%d_%H%M%S")
    activity_Name = driver.current_activity
    filename = activity_Name + timeStamp
    driver.save_screenshot(path)
    gf.capture_screenshot(gf.driver, "C:\\Users\\Subbareddy\\PycharmProjects\\AppiumPractise\\ScreenShots\\"+filename+".png",)
    return driver'''

def longpress(driver, element):
    actions = TouchAction(driver)
    actions.long_press(element)
    actions.perform()
    return driver

def hidekeyboard(driver):
    driver.hide_keyboard()

def use_keyboard(driver, keynum):
    driver.press_keycode(keynum)