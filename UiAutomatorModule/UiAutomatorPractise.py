import subprocess
from uiautomator import Device
import time

d = Device('P2L4C17B27000826')
x = subprocess.call("adb devices", shell=True)
print("Return Code of adb command is : ", x)
d.screen.on()
time.sleep(2)
coordinates = []
coordinates[0] = [205, 1343]
coordinates[0] = [545, 1343]
coordinates[0] = [847, 1343]
coordinates[0] = [210, 1567]
d.swipe(coordinates, 10)
































'''
# wakeup the device, same as turning on the screen.
d.wakeup()
# after 2 seconds turning off the screen
time.sleep(2)
# sleep the device, same as turning off the screen.
d.sleep()
'''
'''
# to perform screen on
d.screen.on()
# after 3 seconds turning off the screen
time.sleep(3)
# to perform screen off
d.screen.off()

#print(d.info)

'''
