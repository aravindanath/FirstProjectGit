from uiautomator import device as d
from uiautomator import Device
import subprocess
from time import sleep
d = Device("P2L4C17B27000826")


def launch_dialer():
    sleep(1)
    launcher = subprocess.Popen("adb shell am start -a android.intent.action.MAIN -n "
                                "com.android.contacts/com.android.contacts.activities.DialtactsActivity",
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if launcher.returncode == 0:
        print("Test Case-1 Result: Sorry! Unable to launch Dialer App (FAILED)")
    else:
        print("Test Case-1 Result: Dialer App launched successfully (PASS)")
        print("==============================================")


def voice_call_functionality():
    print("Execution Started for this Script --> VoiceCall.py: ")
    print("==============================================")
    print("Test Case-1: Trying to launch Dialer App : ")
    launch_dialer()
    sleep(2)
    try:
        print("Test Case-2: Calling to Help-Line number or to Any other phone number: ")
        d(text="1").click()
        d(text="9").click()
        d(text="9").click()
        # press call button
        d(resourceId="com.android.contacts:id/dialButton", className="android.widget.ImageButton").click()
        print("Test Case-2 Result: Phone call connected  : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-2 Result: Not able to connect to Phone call : (FAILED) ")


def hold_call():
    sleep(2)
    print("Test Case-3: Performing call hold and un-hold operation :")
    try:
        # hold call
        d(resourceId="com.android.incallui:id/holdButton").click()
        sleep(3)
        # un-hold call
        d(resourceId="com.android.incallui:id/holdButton").click()
        print("Test Case-3 Result: Phone call hold and un-hold operation done successfully : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-3 Result: Not able to perform call hold and un-hold operation : (FAILED) ")


def mute_call():
    sleep(1)
    print("Test Case-4: Performing call mute and un-mute operation :")
    try:
        # mute call
        d(resourceId="com.android.incallui:id/muteButton").click()
        sleep(3)
        # un-mute call
        d(resourceId="com.android.incallui:id/muteButton").click()
        print("Test Case-4 Result: Phone call mute and un-mute operation done successfully : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-4 Result: Not able to perform call mute and un-mute operation : (FAILED) ")


def call_recording():
    sleep(1)
    print("Test Case-5: Performing call recording operation :")
    try:
        # start recording
        d(resourceId="com.android.incallui:id/recordButton").click()
        sleep(4)
        # stop recording
        d(resourceId="com.android.incallui:id/recordButton").click()
        print("Test Case-5 Result: Phone call recording operation done successfully : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-5 Result: Not able to perform call recording operation : (FAILED) ")


def speaker_on_off():
    sleep(1)
    print("Test Case-6: Performing Speaker on and off operation during call:")
    try:
        # speaker on
        d(resourceId="com.android.incallui:id/showAudioButton").click()
        sleep(4)
        # speaker off
        d(resourceId="com.android.incallui:id/showAudioButton").click()
        print("Test Case-6 Result: Speaker on and off operation done successfully during call : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-6 Result: Not able to perform Speaker on and off operation during call : (FAILED) ")


def call_end():
    sleep(1)
    print("Test Case-7: Performing Phone Call End operation:")
    try:
        # Call Ending
        d(resourceId="com.android.incallui:id/endButton").click()
        sleep(2)
        print("Test Case-7 Result: Phone Call End operation done successfully : (PASS) ")
        print("==============================================")
    except:
        print("Test Case-7 Result: Not able to perform Phone Call End operation : (FAILED) ")

    d.press.home()
    print("Yeah! Came back to home menu")


voice_call_functionality()
hold_call()
mute_call()
call_recording()
speaker_on_off()
call_end()
print("Finally. Your test is completed....")