# RokuTV With Appium — TestMu AI (Formerly LambdaTest)

<p align="center">
  <a href="https://www.testmuai.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Blog</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Docs</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Learning Hub</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/newsletter/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Newsletter</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.testmuai.com/certifications/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv" target="_bank">Certifications</a>
  &nbsp; &#8901; &nbsp;
  <a href="https://www.youtube.com/@TestMuAI" target="_bank">YouTube</a>
</p>
&emsp;
&emsp;
&emsp;

_Appium is a tool for automating native, mobile web, and hybrid applications on iOS, Android, and Windows platforms. It supports iOS native apps written in Objective-C or Swift and Android native apps written in Java or Kotlin. It also supports mobile web apps accessed using a mobile browser (Appium supports Safari on iOS and Chrome or the built-in 'Browser' app on Android). Perform Appium automation tests on [TestMu AI's online cloud](https://www.testmuai.com/appium-mobile-testing?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)._

_Learn the basics of [Appium testing on the TestMu AI platform](https://www.testmuai.com/support/docs/getting-started-with-appium-testing/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)._

[<img height="53" width="200" src="https://user-images.githubusercontent.com/70570645/171866795-52c11b49-0728-4229-b073-4b704209ddde.png">](https://accounts.lambdatest.com/register?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Run Your First Test](#run-your-first-test)
- [Executing The Tests](#executing-the-tests)


## Pre-requisites

### Setting Up Your Authentication

Make sure you have your TestMu AI credentials with you to run test automation scripts on LambdaTest. To obtain your access credentials, [purchase a plan](https://billing.lambdatest.com/billing/plans?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv) or access the [Automation Dashboard](https://appautomation.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

Set TestMu AI `Username` and `Access Key` in environment variables.

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

Upload your **Roku TV** application (.zip file) to the TestMu AI servers using our **REST API**. You need to provide your **Username** and **AccessKey** in the format `Username:AccessKey` in the **cURL** command for authentication. Make sure to add the path of the **appFile** in the cURL request. Here is an example cURL request to upload your app using our REST API:

 **Using App File from System:**
 
 ```bash
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "appFile=@"/Users/macuser/Downloads/roku-sample-app.zip"" F "name=roku-sample-app"
```

**Using App URL:**

```
curl -u "YOUR_LAMBDATEST_USERNAME:YOUR_LAMBDATEST_ACCESS_KEY" -X POST "https://manual-api.lambdatest.com/app/upload/realDevice" -F "url=:https://prod-mobile-artefacts.lambdatest.com/assets/docs/roku-sample-app.zip" -F "name=roku-sample-app"
```

> [!TIP]
> - If you do not have any **.zip** file, you can run your sample tests on TestMu AI by using our sample :link: [RokuTV app](https://prod-mobile-artefacts.lambdatest.com/assets/docs/roku-sample-app.zip).
> - Response of above cURL will be a **JSON** object containing the `APP_URL` of the format - <lt://APP123456789123456789> and will be used in the next step

## Run Your First Test

Once you are done with the above-mentioned steps, you can initiate your first rokutv test on LambdaTest.

**Test Scenario:** Check out the [sample_test.py](https://github.com/LambdaTest/LT-appium-rokutv/blob/master/sample_test.py) file to view the sample test script. 

### Configuring Your Test Capabilities

You can update your custom capabilities in test scripts. In this sample project, we are passing platform name, platform version, device name and app url (generated earlier) along with other capabilities like build name and test name via capabilities object. The capabilities object in the sample code are defined as:

```python title="sample_test.py"
    desired_caps = {
        "automationName": "Roku",
        "deviceName" : "Roku Express",    # We also support "Roku Ultra"
        "platformVersion" :  "11",
        "platformName" : "roku",
        "isRealMobile":True,
        "build": "Roku Sample Test",
        "app":"APP_URL",                  # Enter app url here
        "devicelog": True,
        "privateCloud": True,
        "visual" : True
    }
```

**Info Note:**

- You must add the generated **APP_URL** to the `"app"` capability in the config file.
- You can generate capabilities for your test requirements with the help of our inbuilt **[Capabilities Generator tool](https://www.testmuai.com/capabilities-generator/beta/index.html?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)**. A more Detailed Capability Guide is available [here](https://www.testmuai.com/support/docs/desired-capabilities-in-appium/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

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
> ```
> pip3 install virtualenv
> virtualenv venv
> source venv/bin/activate
> ```

Your test results would be displayed on the test console (or command-line interface if you are using terminal/cmd) and on the [TestMu AI App Automation Dashboard](https://appautomation.lambdatest.com/build?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv).

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
- [How to integrate TestMu AI with CI/CD](https://www.testmuai.com/support/docs/integrations-with-ci-cd-tools/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## Documentation & Resources :books:

Visit the following links to learn more about TestMu AI's features, setup and tutorials around test automation, mobile app testing, responsive testing, and manual testing.

- [TestMu AI Documentation](https://www.testmuai.com/support/docs/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)
- [TestMu AI Blog](https://www.testmuai.com/blog/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)
- [TestMu AI Learning Hub](https://www.testmuai.com/learning-hub/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv)

## TestMu AI Community :busts_in_silhouette:

The [TestMu AI Community](https://community.testmuai.com/?utm_source=github&utm_medium=repo&utm_campaign=LT-appium-rokutv) allows people to interact with tech enthusiasts. Connect, ask questions, and learn from tech-savvy people. Discuss best practises in web development, testing, and DevOps with professionals from across the globe 🌎

## What's New At TestMu AI ❓

To stay updated with the latest features and product add-ons, visit [Changelog](https://changelog.lambdatest.com/)

## 🚀 LambdaTest is Now TestMu AI

👋 Welcome to TestMu AI, the next evolution of LambdaTest. As of January 2026, [LambdaTest is Now TestMu AI](https://www.testmuai.com/lambdatest-is-now-testmuai/) - we have evolved from a cross-browser testing cloud into a unified, AI-native quality engineering platform designed for the modern DevOps era.

Whether you have been part of the LambdaTest community for years or are just discovering TestMu AI, our mission remains the same: to help you ship faster with high-scale test execution, autonomous testing, and deep quality analytics.

### 🔄 Our Rebrand Journey

In 2017, we introduced LambdaTest with a clear mission: to become the world's most trusted cloud testing platform. We built a scalable, high-performance test cloud that eliminated flakiness, improved developer feedback cycles, and accelerated release velocity for teams worldwide.

As LambdaTest grew, we expanded the platform into Test Intelligence, Visual Regression Testing, Accessibility Testing, API Testing, and Performance Testing, covering the entire testing lifecycle. These capabilities enabled teams to test any stack, on any technology, at enterprise scale.

Over time, we rebuilt the architecture to be AI-native from the ground up. What began as LambdaTest's high-performance testing cloud has now evolved into TestMu AI, an AI-native, multi-agent platform redefining modern quality engineering.

We chose the name TestMu AI to reflect our shift towards intelligent, autonomous testing. While our identity has changed, our core technology and commitment to the testing community stay the same.

👉 Find [LambdaTest's New Home](https://www.testmuai.com/).

### 🔭 Explore TestMu AI

The same infrastructure LambdaTest customers relied on, now delivered through autonomous AI agents.

- [KaneAI](https://www.testmuai.com/kane-ai/)
- [Agent-to-Agent Testing](https://www.testmuai.com/agent-to-agent-testing/)
- [HyperExecute](https://www.testmuai.com/hyperexecute/)
- [Real Device Cloud](https://www.testmuai.com/real-device-cloud/)
- [Pricing](https://www.testmuai.com/pricing/)
- [Documentation](https://www.testmuai.com/support/docs/)