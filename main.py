from webDriver import WebDriver
import time
import os

def run(hub_url: str, caps: dict):
    try:
        web_driver = WebDriver(hub_url, caps)


        web_driver.apps()
        time.sleep(5)
        web_driver.launch_the_channel("dev")

        for i in range(5):
            t = time.time()
            web_driver.press_btn("select")
            t2 = time.time()
            print("select time :",t2-t)
            time.sleep(2)


        web_driver.quiet()
        print("Test passed")
    except  Exception as e:
        print(f"Error: {e}")
        print("Test failed")
    
if __name__ == "__main__":

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accessToken = "accessToken"
    else:
        accessToken = os.environ.get("LT_ACCESS_KEY")

    hub_url = "mobile-hub-internal.lambdatest.com/wd/hub/session"

    url = "http://"+username+":"+accessToken+"@"+hub_url
    
    caps = {
        "deviceName": "Roku Express",
        "platformVersion": "11",
        "isRealMobile": True,
        "platformName": "roku",
        "build": "Roku Sample Test",
        "app": "APP_URL",          #Add app url here
        "video": True,
        "visual": True,
        "devicelog": True
    }
    t1 = time.time()
    run(url, caps)
    t2 = time.time()
    print("sec:",t2-t1)
