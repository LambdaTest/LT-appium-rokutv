# RokuTV With Appium

<p align="center">
  <a href="https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.lambdatest.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/c/LambdaTest" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

_Appium is a tool for automating native, mobile web, and hybrid applications on iOS, Android, and Windows platforms. It supports iOS native apps written in Objective-C or Swift and Android native apps written in Java or Kotlin. It also supports mobile web apps accessed using a mobile browser (Appium supports Safari on iOS and Chrome or the built-in 'Browser' app on Android). Perform Appium automation tests on [LambdaTest's online cloud](https://www.lambdatest.com/appium-mobile-testing?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)._

_Learn the basics of [Appium testing on the LambdaTest platform](https://www.lambdatest.com/support/docs/getting-started-with-appium-testing/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)._

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Run Your First Test](#run-your-first-test)
- [Executing The Tests](#executing-the-tests)


## Pre-requisites

### Setting Up Your Authentication

Make sure you have your LambdaTest credentials with you to run test automation scripts on LambdaTest. To obtain your access credentials, [purchase a plan](https://billing.lambdatest.com/billing/plans?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv) or access the [Automation Dashboard](https://appautomation.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

Set LambdaTest `Username` and `Access Key` in environment variables.

**For Linux/macOS:**

```bash
export LT_USERNAME=YOUR_LAMBDATEST_USERNAME \
export LT_ACCESS_KEY=YOUR_LAMBDATEST_ACCESS_KEY
```

**For Windows:**

```powershell
set LT_USERNAME=YOUR_LAMBDATEST_USERNAME `
set LT_ACCESS_KEY=YOUR_LAMBDATEST_ACCESS_KEY
```

### Upload Your Application

Upload your **Roku TV** application (.zip file) to the LambdaTest servers using our **REST API**. You need to provide your **Username** and **AccessKey** in the format `Username:AccessKey` in the **cURL** command for authentication. Make sure to add the path of the **appFile** in the cURL request. Here is an example cURL request to upload your app using our REST API:

 **Using App File from System:**
 
 ```bash
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "appFile=@"/Users/macuser/Downloads/roku-sample-app.zip"" F "name=roku-sample-app"
```

**Using App URL:**

```
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "url=:https://prod-mobile-artefacts.lambdatest.com/assets/docs/roku-sample-app.zip" -F "name=roku-sample-app"
```

> [!TIP]
> - If you do not have any **.zip** file, you can run your sample tests on LambdaTest by using our sample :link: [RokuTV app](https://prod-mobile-artefacts.lambdatest.com/assets/docs/roku-sample-app.zip).
> - Response of above cURL will be a **JSON** object containing the `APP_URL` of the format - <lt://APP123456789123456789> and will be used in the next step

## Run Your First Test

Once you are done with the above-mentioned steps, you can initiate your first rokutv test on LambdaTest.

**Test Scenario:** Check out [sample_test.py](https://github.com/LambdaTest/LT-appium-rokutv/blob/master/main.py) file to view the sample test script. 

### Configuring Your Test Capabilities

You can update your custom capabilities in test scripts. In this sample project, we are passing platform name, platform version, device name and app url (generated earlier) along with other capabilities like build name and test name via capabilities object. The capabilities object in the sample code are defined as:

```python title="sample_test.py"
    desired_caps = {
        "automationName": "Roku",
        "deviceName" : "Roku Express",    #We also support "Roku Ultra"
        "platformVersion" :  "11",
        "platformName" : "roku",
        "isRealMobile":True,
        "build": "Roku Sample Test",
        "app":"APP_URL",                  #Enter app url here
        "devicelog": True,
        "privateCloud": True,
        "visual" : True
    }
```

**Info Note:**

- You must add the generated **APP_URL** to the `"app"` capability in the config file.
- You can generate capabilities for your test requirements with the help of our inbuilt **[Capabilities Generator tool](https://www.lambdatest.com/capabilities-generator/beta/index.html?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)**. A more Detailed Capability Guide is available [here](https://www.lambdatest.com/support/docs/desired-capabilities-in-appium/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

## Executing The Tests

1. Install the required packages from the cloned project directory:

```bash
pip install -r requirements.txt
```

2. Run the following command in the directory where your project has been saved to execute your build.

```python
python main.py
```

> [!TIP]
> If you are unable to run the automation script with the above mentioned commands try **'python3'** command except for **'python'**.

> [!TIP]
> If you fail to run the tests, try creating virtual env and installing the dependencies in that environment to run the tests.
> Creating and activating a virtual environment

```
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on the [LambdaTest App Automation Dashboard](https://appautomation.lambdatest.com/build?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

## Supported Commands

We utilise the Appium Roku Driver to run tests on Roku via Appium, here's a list of all the commands the driver supports from the project's [README](https://github.com/headspinio/appium-roku-driver?tab=readme-ov-file#roku-commands):

|Command|Parameters|Description|
|-------|----------|-----------|
|`roku: pressKey`|`key`|Press the remote key whose value matches `key` (must be one of the [supported key values](https://developer.roku.com/en-ca/docs/developer-program/debugging/external-control-api.md#keypress-key-values) from the Roku documentation). As addressed in the documentation, Roku TVs also support additioanl keys such as `PowerOff` and `PowerOn`. |
|`roku: deviceInfo`||Get information about the Roku device|
|`roku: getApps`||Get a list of apps installed on the device. The response will be a list of objects with the following keys: `id`, `type`, `subtype`, `version`, and `name`.|
|`roku: activeApp`||Get information about the active app, in the same format as `roku: getApps`.|
|`roku: activateApp`|`appId` (required), `contentId`, `mediaType`|Launch an app with the corresponding `appId`. Optionally include `contentId` and `mediaType` information (with the same properties as described above for the `activateApp` command)|
|`roku: selectElement`|`elementId` (required) |Moves the focus on a element having locator xpath as `elementId`. If it is unable to focus on the element, the driver will respond with a error.|
|`roku: playerState`||Get the state of the media player. The data will be returned as a JSON object, corresponding to the information included in the [query/media-player ECP result](https://developer.roku.com/en-ca/docs/developer-program/dev-tools/external-control-api.md#querymedia-player-example)|
|`roku: deepLink`|`contentId`, `mediaType`|As described in the [Roku dev docs](https://developer.roku.com/en-ca/docs/developer-program/discovery/implementing-deep-linking.md#using-ecp-commands-for-testing-deep-linking), you can deep link into content in the running application using a content ID and media type. For this command, `contentId` is required, and `mediaType` defaults to `movie` and must be one of the [valid media types](https://developer.roku.com/en-ca/docs/developer-program/discovery/implementing-deep-linking.md#mediatype-behavior). Note that this command acts on the currently-running app. If you want to test deep-linking into an app that is not launched, use `activateApp` instead.|
|`roku: ecpInput`|`params`|This command allows calling the `/input` ECP command directly. An arbitrary set of key/value pairs can be sent in as a JSON object. No url-encoding of the values needs to be done. For example, to represent the parameters in the ECP command `POST /input?acceleration.x=0.0&acceleration.y=0.0&acceleration.z=9.8` from the ECP docs, you would construct a `params` of `{"acceleration.x": "0.0", "acceleration.y": "0.0", "acceleration.z": "9.8"}`|



## Additional Links

- [Appium Roku Driver](https://github.com/headspinio/appium-roku-driver)
- [How to integrate LambdaTest with CI/CD](https://www.lambdatest.com/support/docs/integrations-with-ci-cd-tools/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## Documentation & Resources :books:

Visit the following links to learn more about LambdaTest's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

- [LambdaTest Documentation](https://www.lambdatest.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)
- [LambdaTest Blog](https://www.lambdatest.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)
- [LambdaTest Learning Hub](https://www.lambdatest.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## LambdaTest Community :busts_in_silhouette:

The [LambdaTest Community](https://community.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At LambdaTest ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/)

## About LambdaTest

[LambdaTest](https://www.lambdatest.com?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv) is a leading test execution and orchestration platform that is fast, reliable, scalable, and secure. It allows users to run both manual and automated testing of web and mobile apps across 3000+ different browsers, operating systems, and real device combinations. Using LambdaTest, businesses can ensure quicker developer feedback and hence achieve faster go to market. Over 500 enterprises and 1 Million + users across 130+ countries rely on LambdaTest for their testing needs.

### Features

- Run Selenium, Cypress, Puppeteer, Playwright, and Appium automation tests across 3000+ real desktop and mobile environments.
- Real-time cross browser testing on 3000+ environments.
- Test on Real device cloud
- Blazing fast test automation with HyperExecute
- Accelerate testing, shorten job times and get faster feedback on code changes with Test At Scale.
- Smart Visual Regression Testing on cloud
- 120+ third-party integrations with your favorite tool for CI/CD, Project Management, Codeless Automation, and more.
- Automated Screenshot testing across multiple browsers in a single click.
- Local testing of web and mobile apps.
- Online Accessibility Testing across 3000+ desktop and mobile browsers, browser versions, and operating systems.
- Geolocation testing of web and mobile apps across 53+ countries.
- LT Browser - for responsive testing across 50+ pre-installed mobile, tablets, desktop, and laptop viewports

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## We are here to help you :headphones:

- Got a query? we are available 24x7 to help. [Contact Us](mailto:support@lambdatest.com)
- For more info, visit - [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)
