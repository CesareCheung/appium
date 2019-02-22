from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# region 连接appium
# appium服务器地址
command_executor = "http://127.0.0.1:4723/wd/hub"

# 所需能力:http://appium.io/docs/cn/writing-running-appium/caps/index.html
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7",
    "deviceName": "android",
    "newCommandTimeout": "60000",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "appPackage": "io.github.liushilive.at",
    "appActivity": ".MainActivity"
    # "app": "at.apk"
    # "app": "https://github.com/liushilive/liushilive.github.io/releases/download/v2.0/app-v2.0.apk"
}

driver = webdriver.Remote(
    command_executor=command_executor,
    desired_capabilities=desired_capabilities
)
# endregion

# region 应用相关
# http://appium.io/docs/cn/writing-running-appium/appium-bindings/
# 判断app是否已经安装
print(driver.is_app_installed("io.github.liushilive.at"))
# 卸载
driver.remove_app("io.github.liushilive.at")
# 安装
driver.install_app("https://github.com/liushilive/liushilive.github.io/releases/download/v2.0/app-v2.0.apk")
#  启动app
driver.start_activity("io.github.liushilive.at", ".MainActivity")
# endregion

# region 查找元素
# resource-id
ele = driver.find_element_by_id("type_text_button")
# content-desc
ele = driver.find_element_by_accessibility_id("文本类型")
ele = driver.find_element_by_xpath("//*[@text='文本类型']")
ele = driver.find_element_by_xpath("//*[@index='1']")
ele = driver.find_element_by_class_name("android.widget.Button")
# ele = driver.find_element_by_image("1.png")
# endregion

# region 文本类型
ele = driver.find_element_by_id("type_text_button")
# 元素大小
print(ele.size)
# 元素位置
print(ele.location)
# 点击元素
ele.click()
# 输入文本
ele = driver.find_element_by_id("name_edittext")
ele.send_keys(123)
ele.send_keys("刘")
ele.text
# 清空
ele.clear()
# 点击Next
driver.find_element_by_id("next_button").click()
# 获取提示值
driver.find_element_by_id("error_text").text
# 后退
driver.find_element_by_id("menu_item_back").click()
# endregion

# region 下拉菜单
driver.find_element_by_id("下拉菜单").click()
driver.find_element_by_id("countries_spinner").click()
driver.find_element_by_xpath("//*[@text='中国']").click()
driver.find_element_by_id("menu_item_back").click()

# endregion

# region 书籍列表
driver.find_element_by_accessibility_id("书籍列表").click()
eles = driver.find_elements_by_id("book_title")
for ele in eles:
    print("书名：", ele.text)

ele = driver.find_element_by_xpath("//*[contains(@text, 'Agile Web Development with Rails 4')]")

ele = driver.find_element_by_android_uiautomator(
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Agile Web Development with Rails 4"))'
)
# endregion

# region 对话框
driver.find_element_by_id("confirm_dialog_button").click()
driver.find_element_by_id("button1").click()
# endregion

# region 日期时间
# 点出日期选择器
driver.find_element_by_id("date_picker_button").click()
# 点击年
driver.find_element_by_id("date_picker_header_year").click()
# 滑动器
ele = driver.find_element_by_id("date_picker_year_picker")
x = ele.rect.get("x")
y = ele.rect.get("y")
h = ele.rect.get("height")
while True:
    if '2010' in driver.page_source:
        break
    driver.swipe(x, y + 10, x, h - 10, 2000)
driver.find_element_by_xpath("//*[@text='2010']").click()

# 选择月
while True:
    # get_attribute("name") 返回元素的content-desc属性值
    if '十月' in driver.find_element_by_xpath("//*[@resource-id='android:id/month_view']/*").get_attribute("name"):
        break
    driver.find_element_by_id("next").click()
# 选择日
driver.find_element_by_xpath("//android.view.View[@text=21]").click()
# 点击确认
driver.find_element_by_id("button1").click()

# 时间选择器
driver.find_element_by_id("time_picker_button").click()
driver.find_element_by_id("time_header").send_keys("2230")
driver.find_element_by_id("button1").click()
# endregion

# region 画布
# 短按 press
# 释放 release
# 移动 moveTo
# 点击tap
# 长按 longPress
# 等待 wait
# 取消 cancel
# 执行 perform

ele = driver.find_element_by_id("finger_view")
x = ele.rect.get("x")
y = ele.rect.get("y")
w = ele.rect.get("width")
h = ele.rect.get("height")

# 单点触摸
TouchAction(driver).press(x=x + 100, y=y + 100) \
    .move_to(x=x + 100, y=y + 200).wait(3000) \
    .move_to(x=x + 200, y=y + 500).wait(3000) \
    .release().perform()

# 多点触摸
from appium.webdriver.common.multi_action import MultiAction

x1, y1, x2, y2 = 100, y + 100, 300, y + 100
ac0 = TouchAction(driver).press(x=x1, y=y1).wait(10)
ac1 = TouchAction(driver).press(x=x2, y=y2).wait(10)
for i in range(5):
    y1 += 50
    ac0.move_to(x=x1, y=y1).wait(10)
    x1 += 50
    ac0.move_to(x=x1, y=y1).wait(10)
    y2 += 50
    ac1.move_to(x=x2, y=y2).wait(10)
    x2 += 50
    ac1.move_to(x=x2, y=y2).wait(10)
ac0.wait(2000).release()
ac1.wait(5000).release()

m = MultiAction(driver)
m.add(ac0, ac1)
m.perform()
# endregion

# region 手势
# 长按
ele = driver.find_element_by_id("long_press_button")
TouchAction(driver).long_press(ele).release().perform()

# 滑动
ele = driver.find_element_by_id("seekBar1")
x = ele.rect.get("x")
y = ele.rect.get("y")
w = ele.rect.get("width")
TouchAction(driver).press(x=x, y=y).wait(1000) \
    .move_to(x=x + w, y=y).wait(1000) \
    .move_to(x=x + w / 10, y=y) \
    .release().perform()

ele = driver.find_element_by_id("seekBar2")
x = ele.rect.get("x")
y = ele.rect.get("y")
w = ele.rect.get("width")
TouchAction(driver).press(x=x, y=y).wait(1000) \
    .move_to(x=x + w, y=y).wait(1000) \
    .move_to(x=x + w / 10, y=y) \
    .release().perform()
# endregion

# region 其他
# 键盘按键
driver.keyevent(4)
# 放到后台运行
driver.background_app(seconds=5)
# endregion

# region 文件上传
# 上传文件
import base64

with open("1.png", 'rb') as f:
    path = '/storage/emulated/0/1.png'
    data = base64.b64encode(f.read())
    driver.push_file(path, str(data, "utf-8"))
# endregion

# region 缩放
# 缩放
x = driver.get_window_size().get("width") / 2
y = driver.get_window_size().get("height") / 2
ac1 = TouchAction(driver).press(x=x, y=y - 100).wait(500) \
    .move_to(x=x, y=y - y / 2).wait(500).release()
ac2 = TouchAction(driver).press(x=x, y=y + 100).wait(500) \
    .move_to(x=x, y=y + y / 2).wait(500).release()
m = MultiAction(driver)
m.add(ac1, ac2)
m.perform()
# endregion

# region webview
w = driver.get_window_size().get("width")
h = driver.get_window_size().get("height")
# 侧滑
driver.swipe(1, h / 2, w / 2, h / 2)
driver.find_element_by_xpath("//*[@text='WebView']").click()

# 当前上下文
driver.context
driver.contexts

# 进入 webview
driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
driver.find_element_by_partial_link_text("HTMLreport").click()
# 跳出
driver.switch_to.context("NATIVE_APP")
driver.switch_to.context(None)

# endregion

# region 关闭app 断开appium服务
driver.close_app()
driver.quit()
# endregion
