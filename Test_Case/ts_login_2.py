import time
import unittest
from appium import webdriver
from HTMLReport import logger
from Common.appium_api import add_image

from Business.url import dsc_app_index, command_executor, desired_capabilities


class TS_Login(unittest.TestCase):
    def setUp(self):
        logger().info(f"appium服务器：{command_executor}")
        logger().info(f"appium 参数：{desired_capabilities}")
        self.driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=desired_capabilities
        )
        self.driver.implicitly_wait(5)
        add_image(self.driver)

    def tearDown(self):
        logger().info("关闭APP并退出")
        self.driver.quit()

    def test_login_1(self):
        username = "liu01"
        password = "123456"
        driver = self.driver
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
            driver.swipe(1, h / 2, w / 2, h / 2)
            add_image(driver)
            logger().info("点击大商创")
            driver.find_element_by_xpath("//*[@text='大商创']").click()
        add_image(driver)
        logger().info("进入webview")
        driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
        time.sleep(2)
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

        time.sleep(2)
        add_image(driver)
        logger().info("断言 进入首页")
        self.assertEqual("首页", driver.title)
        logger().info("断言 个人中心")
        driver.find_element_by_xpath("//*[text()='我']/../a").click()
        add_image(driver)
        self.assertEqual("个人中心", driver.title)
        logger().info("断言 用户名")
        driver.find_element_by_xpath('//*[@class="header-admin"]/h4').click()
        add_image(driver)
        text = driver.find_element_by_xpath("//*[text()='用户名']/..").text
        self.assertIn(username, text)
        pass

    def test_login_2(self):
        username = ""
        password = "123456"
        driver = self.driver
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
            driver.swipe(1, h / 2, w / 2, h / 2)
            add_image(driver)
            logger().info("点击大商创")
            driver.find_element_by_xpath("//*[@text='大商创']").click()
        add_image(driver)
        logger().info("进入webview")
        driver.switch_to.context("WEBVIEW_io.github.liushilive.at")
        time.sleep(2)
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

        logger().info("断言 请输入用户名")
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("请输入用户名", text)
        add_image(driver)
        pass
