import time
import unittest
from appium import webdriver
from HTMLReport import logger

from Business.login_process import open_dsc, login
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
        username = "111"
        password = "123456"
        driver = self.driver

        open_dsc(driver)

        login(driver, username, password)

        time.sleep(2)
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
        username = "liu011"
        password = "123456"
        driver = self.driver

        open_dsc(driver)

        login(driver, username, password)

        logger().info("断言 请输入用户名")
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("请输入用户名", text)
        add_image(driver)
        pass

    def test_login_3(self):
        username = "liu011"
        password = "1234567"
        driver = self.driver

        open_dsc(driver)

        login(driver, username, password)

        logger().info("断言 用户名或密码错误")
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("用户名或密码错误", text)
        add_image(driver)
        pass

    def test_login_4(self):
        username = "liu011"
        password = ""
        driver = self.driver

        open_dsc(driver)

        login(driver, username, password)

        logger().info("断言 请输入密码")
        text = driver.find_element_by_class_name("layermcont").text
        self.assertEqual("请输入密码", text)
        add_image(driver)
        pass
