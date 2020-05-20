from appium import webdriver
global driver
# adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"
desired_caps = {
    "platformName": "Android",
    "deviceName": "Honor7X",
    #"deviceName": "Redmi",
    "noReset": True,
    "udid": "P2L4C17B27000826",
    #"udid": "203a43ac7ce4",
    "noSign": True,
    "autoGrantPermissions": True,
    "automationName": "UiAutomator2",
    #"platformVersion": "7.1.2",
    "platformVersion": "9",
    # com.android.calendar/com.android.calendar.homepage.AllInOneActivity
    # com.androidsample.generalstore/com.androidsample.generalstore.SplashActivity
    # com.android.mms/com.android.mms.ui.MmsTabActivity
    # com.android.camera/com.android.camera.Camera
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.HWSettings"
    #"app": "E:\\Python\\APK\\GeneralStore.apk"
}
driver = webdriver.Remote("http://127.0.0.1:4586/wd/hub", desired_caps)
driver.implicitly_wait(30)
print("App Launched")
