import subprocess
from uiautomator import device as d
import time

def messageAppOpen():
    app_Open = subprocess.Popen("adb shell am start -a android.intent.action.MAIN -n com.google.android.apps.messaging/com.google.android.apps.messaging.ui.ConversationListActivity",
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    if app_Open.returncode:
        print("Message app is unable to launch:")
    else:
        if d.exists(text="Messages"):
            time.sleep(2)
            #d.press.back()
            print("Message app is launched successfully:")
        app_Open.stdout.close()


def clickStartChat():
    print("TestCase1:- To verify user can click on Start chat button")
    print("Execution Started:")
    messageAppOpen()
    try:
        if d(className="android.widget.Button").click():
            time.sleep(2)
            print("Clicked on Start Chat button successfully:")
            print("Trying to enter text:")
            d(text="Type a name, phone number or email address").set_text("9948887542")
            time.sleep(1)
            d.press.enter()
            #d(resourceID="com.google.android.apps.messaging:id/contact_detail_type").click()
            #time.sleep(2)
            d(className="android.widget.EditText").set_text("Hai Dad, How are you?")
            time.sleep(2)
            #d.press.enter()
            d(text="SMS").click()
            #time.sleep(2)
            print("Message sent successfully")
            #d.press.enter()
    except:

        print("Test case failed, not able to click on Start Chat button")


clickStartChat()
