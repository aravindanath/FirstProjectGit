import subprocess
from uiautomator import Device
import time


d = Device("P2L4C17B27000826")


def settings_app_launch():
    # first we need to open settings
    # adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"
    # use above adb command to get desired app package and app activity name
    launcher = subprocess.Popen("adb shell am start -a android.intent.action.MAIN -n "
                                "com.android.settings/com.android.settings.HWSettings",
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(3)
    if launcher.returncode:
        print("Test Case-1 Result: Sorry! Unable to launch Settings App (FAILED)")
    else:
        print("Test Case-1 Result: Settings App launched successfully (PASS)")
        print("==============================================")


def scrolling_check():
    print("Execution Started for this Script --> fdfsssg.py: ")
    print("==============================================")
    print("Test Case-1: Trying to launch Settings App: ")
    settings_app_launch()
    time.sleep(2)
    try:
        print("Test Case-2: Performing Scroll down operation in Settings App: ")
        # performing scrolling operation here
        d(scrollable=True).scroll.to(text="System")
        time.sleep(2)
        print("Test Case-2 Result: Scroll down operation completed successfully in Settings App : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-2 Result: Scroll down operation not able to complete : (FAILED) ")


def click_on_system_menu():
    scrolling_check()
    time.sleep(2)
    print("Test Case-3: Trying to click on System menu in Settings App: ")
    try:
        d(text="System", className="android.widget.TextView").click()
        print("Test Case-3 Result: System menu opened successfully : (PASS)")
        print("==============================================")
        time.sleep(2)
        print("Test Case-4: Trying to click on Certification logos menu under System menu : ")
        # again scrolling here
        d(scrollable=True).scroll.to(text="Certification logos")
        d(text="Certification logos", className="android.widget.TextView").click()
        print("Test Case-4 Result: Certification logos menu opened successfully under System menu  : (PASS)")
        print("==============================================")
        time.sleep(3)
        d.press.home()
        print("Yeah! finally came back to Home Menu")
    except:
        print("Test Case-3 Result: System menu not opened : (FAILED)")


click_on_system_menu()