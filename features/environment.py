import allure
from allure_commons.types import AttachmentType

from selenium import webdriver

from utils.ConfigReader import ConfigReader

config_reader = ConfigReader()
properties = config_reader.get_properties()


def before_scenario(context, driver):
    browser_name = properties.get('General', 'browser')

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(properties.get('General', 'url'))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      , name="failed_screenshot"
                      , attachment_type=AttachmentType.PNG)
