from datetime import datetime
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CommonUtils:
    IMPLICIT_WAIT_TIME = 10
    PAGE_LOAD_TIME = 15
    EXPLICIT_WAIT_BASIC_TIME = 30
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_email_with_time_stamp():
        now = datetime.now()
        new_email = "walkingtree" + now.strftime("%Y-%m-%d_%H-%M-%S") + "@gmail.com"
        CommonUtils.logger.info("get_email_with_time_stamp() invoked and returning new email " + new_email)
        return new_email

    # @staticmethod
    # def take_screenshot(scenario, driver, scenario_name):
    #     src_screenshot = driver.get_screenshot_as_base64()
    #     CommonUtils.logger.info("take_screenshot() invoked, screenshot taken")
    #     return src_screenshot
