cd /D %UserProfile%\AppData\Local\Programs\Appium\resources\app\node_modules\appium
node . -p 5000 --default-capabilities "{\"udid\":\"6ec890a5\"}" --nodeconfig %~dp0appium-server-5000.json --chromedriver-executable %~dp0chromedriver.2.45.exe
