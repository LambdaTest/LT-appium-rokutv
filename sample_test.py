from appium import webdriver
import os
import time
from appium.options.android import UiAutomator2Options


def getCaps():
   desired_caps = {
       "automationName": "Roku",
       "deviceName" : "Roku Ultra",
       "platformVersion" :  "11",
       "platformName" : "roku",
       "isRealMobile":True,
       "build": "Roku Sample Test",
       "app":"APP_URL",     #Enter app url here
       "devicelog": True,
       "privateCloud": True,
       "visual" : True
   }

   return desired_caps


def runTest():
   if os.environ.get("LT_USERNAME") is None:
       # Enter LT username below if environment variables have not been added
       username = "<YOUR_LT_USERNAME>"
   else:
       username = os.environ.get("LT_USERNAME")
   if os.environ.get("LT_ACCESS_KEY") is None:
       # Enter LT accesskey below if environment variables have not been added
       accesskey = "<YOUR_LT_ACCESS_KEY>"
   else:
       accesskey = os.environ.get("LT_ACCESS_KEY")


   # grid url
   gridUrl = "mobile-hub.lambdatest.com/wd/hub"


   # capabilities
   desired_caps = getCaps()
   url = "https://"+username+":"+accesskey+"@"+gridUrl


   print("Initiating remote driver:")
   driver = webdriver.Remote(
       options=UiAutomator2Options().load_capabilities(desired_caps),
       command_executor= url
   )


   # run test
   print(driver.session_id)


   # Simulate remote control actions
   driver.execute_script("roku: pressKey", {"key": "Down"})
   driver.execute_script("roku: pressKey", {"key": "Down"})
   time.sleep(1)
   driver.execute_script("roku: pressKey", {"key": "Right"})
   driver.execute_script("roku: pressKey", {"key": "Up"})
   driver.execute_script("roku: deviceInfo")
   time.sleep(1)
   driver.execute_script("roku: getApps")
   driver.execute_script("roku: pressKey", {"key": "Right"})
   driver.quit()  


if __name__ == "__main__":
   runTest()
