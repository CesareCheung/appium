dsc_app_index = "http://www.xxxx.com"


command_executor = "http://127.0.0.1:4444/wd/hub"

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7",
    "deviceName": "android",
    "newCommandTimeout": "60000",
    "noReset": False,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "appPackage": "io.github.liushilive.at",
    "appActivity": ".MainActivity"
}
