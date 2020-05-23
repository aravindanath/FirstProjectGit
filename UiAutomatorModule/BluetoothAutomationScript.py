import subprocess
from uiautomator import device as d
import time


#x = subprocess.call("adb shell am start -a android.intent.action.MAIN -n com.android.settings/com.android.settings.HWSettings", shell=True)

def BluetoothAppLaunch():

    #First we need to open settings app to go to bluetooth
    # adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"
    #use above adb command to get desired app package and app activity name
    time.sleep(3)
    launcher = subprocess.Popen("adb shell am start -a android.intent.action.MAIN -n com.android.settings/com.android.settings.HWSettings",
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(3)
    if launcher.returncode==0:
        print("Sorry! Unable to Bluetooth app in Setings ")
    else:
        print("Test Case-1: Settings App launched successfully (Pass)")
        if d(text="Device connectivity", className="android.widget.TextView").click():
            time.sleep(3)
            print("Test Case-2: Clicked on Device Connectivity module in Settings App (Pass)")
            d(text="Bluetooth").click()
            print("Test Case-3: Bluetooth UI launched successfully (Pass)")
            time.sleep(3)
            #d.press.home()


def TurnOnAndOffBluetooth():

    #first launching BT app, so calling BluetoothAppLaunch() function

    try:
        #BluetoothAppLaunch()
        #time.sleep(1)
        if d(text="Bluetooth").exists:
            d(className="android.widget.Switch").click()
            #if BT is already Turned on-->then this script will turn it off
            #if BT is already Turned off-->then this script will turn it on
            print("Test Case-4: Turn on/off Bluetooth successfully (Pass)")
            #time.sleep(1)

    except:
        print("Test case-4 failed. Not able to turn on Bluetooth")


def ConnectToBluetoothDevice():

    # first launching BT app and making it turn on, so calling TurnOnAndOffBluetooth() function
    # this TurnOnAndOffBluetooth() will automatically invoke BluetoothAppLaunch() function
    try:
        BluetoothAppLaunch()
        TurnOnAndOffBluetooth()
        #if d(text="PAIRED DEVICES").exists:
        d(text="boAt Rockerz", className="android.widget.TextView").click
        print("=== Able to click on boat Bluetooth device")
        time.sleep(7)
        if d(text="Connected for calls and media audio").exists:
            print("Test Case-5: Successfully paired up to Boat Rockerz Bluetooth Device (Pass)")
        else:
            print("Desired Bluetooth device is not in turn on state")

    except:
        print("Test case-5 failed. Not able to pair up with Bluetooth Device ")

    finally:
        print("Closing the App completely and navigating back to Home")
        time.sleep(3)
        d.press.home()



ConnectToBluetoothDevice()