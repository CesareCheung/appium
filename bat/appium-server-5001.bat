cd /D %UserProfile%\AppData\Local\Programs\Appium\resources\app\node_modules\appium
node . -p 5001 --default-capabilities "{\"udid\":\"CJL7N16127001715\"}" --nodeconfig %~dp0appium-server-5001.json --chromedriver-executable %~dp0chromedriver.2.42.exe
