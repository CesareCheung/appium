from HTMLReport import AddImage, logger
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException


def add_image(driver: WebDriver):
    """截图到报告

    :param driver:
    :return:
    """
    if "NATIVE_APP" in driver.context:
        AddImage(driver.get_screenshot_as_base64())
    else:
        context = driver.context
        driver.switch_to.context(None)
        try:
            AddImage(driver.get_screenshot_as_base64())
        except WebDriverException as e:
            logger().info(f"截图失败：\n{e}")
        finally:
            driver.switch_to.context(context)
