import time

from HTMLReport import logger

from Business.url import dsc_app_index
from Common.appium_api import add_image


def open_dsc(driver):
    logger().info("侧滑进入菜单页")
    w = driver.get_window_size().get("width")
    h = driver.get_window_size().get("height")
    # 侧滑
    driver.swipe(1, h / 2, w / 2, h / 2)
    add_image(driver)
    logger().info("点击大商创")
    driver.find_element_by_xpath("//*[@text='大商创']").click()
    # 获取导航标题的文本
    text = driver.find_element_by_xpath(
        "//*[@resource-id='io.github.liushilive.at:id/toolbar']/android.widget.TextView"
    ).text
    logger().info(f"获取 导航标题的文本：{text}")
    if "设置" in text:
        logger().info("配置IP")
        driver.find_element_by_id("edit_ip").clear()
        driver.find_element_by_id("edit_ip").send_keys(dsc_app_index)
        add_image(driver)
        logger().info("点击保存按钮")
        driver.find_element_by_id("save").click()
        # 侧滑
        driver.swipe(2, h / 2, w / 2, h / 2)
        add_image(driver)
        logger().info("点击大商创")
        driver.find_element_by_xpath("//*[@text='大商创']").click()
    add_image(driver)
    time.sleep(2)
    logger().info("进入webview")
    driver.switch_to.context("WEBVIEW_io.github.liushilive.at")


def login(driver, username, password):
    logger().info("点击 我")
    driver.find_element_by_xpath("//*[text()='我']/../a").click()
    add_image(driver)
    logger().info(f"输入账号:{username}")
    driver.find_element_by_name("username").send_keys(username)
    logger().info("输入密码")
    driver.find_element_by_name("password").send_keys(password)
    add_image(driver)
    logger().info("点击立即登录")
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    # add_image(driver)
