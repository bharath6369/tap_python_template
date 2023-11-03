import pdb
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ElementUtils:
    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.driver = driver
        self.duration_in_seconds = 30  # You can adjust this as needed
        web_element = None

    def click_element(self, locator_type, element):
        web_element = self.get_element(locator_type, element)
        if self.wait_for_element(web_element):
            web_element.click()
        else:
            logging.error("click_element() trigger >>> SEEMS element is not available in dom ", element)

    def clear_and_send_keys(self, locator_type, element, text_to_be_typed):

        web_element = self.get_element(locator_type, element)

        if self.wait_for_element(web_element):
            web_element.click()
            web_element.clear()
            web_element.send_keys(text_to_be_typed)
        else:
            logging.error("clear_and_send_keys() trigger >>> SEEMS element is not available in dom ", element)

    def clear_element(self, locator_type, element):
        web_element = self.get_element(locator_type, element)
        if self.wait_for_element(web_element):
            web_element.clear()
        else:
            logging.error(" web_element.clear()() trigger >>> SEEMS element is not available in dom ", element)

    def wait_for_element(self, web_element):
        status = False
        try:
            wait = WebDriverWait(self.driver, self.duration_in_seconds)
            element = wait.until(EC.visibility_of(web_element))
            if element:
                status = True
            self.logger.info(f"Element is now visible")

        except Exception as e:
            self.logger.error(f"Error waiting for element: {e}")
            status = False

        return status

    def select_option_in_dropdown(self, locator_type, element, drop_down_option):
        web_element = self.get_element(locator_type, element)
        if self.wait_for_element(web_element):
            select = Select(web_element)
            select.select_by_visible_text(drop_down_option)
        else:
            logging.error("select_option_in_dropdown() trigger >>> SEEMS element is not available in dom ", element)

    def accept_alert(self):
        alert = self.wait_for_alert()
        alert.accept()
        self.logger.info("Accepted alert successfully")

    def dismiss_alert(self):
        alert = self.wait_for_alert()
        alert.dismiss()
        self.logger.info("Dismissed alert successfully")

    def wait_for_alert(self):
        alert = None
        try:
            wait = WebDriverWait(self.driver, self.duration_in_seconds)
            alert = wait.until(EC.alert_is_present())
        except Exception as e:
            self.logger.error(f"Error waiting for alert: {e}")
        self.logger.info("Waiting for the alert")
        return alert

    def mouse_hover_and_click(self, locator_type, element):
        web_element = self.get_element(locator_type, element)
        if self.wait_for_element(web_element):
            actions = ActionChains(self.driver)
            actions.move_to_element(web_element).click().perform()
            self.logger.info(f"Mouse-hovered on element {element} and clicked")
        else:
            logging.error("select_option_in_dropdown() trigger >>> SEEMS element is not available in dom ", element)

    def wait_for_visibility_of_element(self, element):
        print('wait for visibility', element)
        web_element = None
        try:
            wait = WebDriverWait(self.driver, self.duration_in_seconds)
            web_element = wait.until(EC.visibility_of(element))
            print("Found web element ", web_element)
        except Exception as e:
            self.logger.error(f"Error waiting for element visibility: {e}")
        self.logger.info("Waiting for the element visibility")
        return web_element

    def javascript_click(self, locator_type, element):
        web_element = self.get_element(locator_type, element)

        if self.wait_for_element(web_element):
            self.driver.execute_script("arguments[0].click();", web_element)
            self.logger.info("Clicked on element using JavaScriptExecutor")
        else:
            logging.error("javascript_click() trigger >>> SEEMS element is not available in dom ", element)

    def javascript_type(self, locator_type, element, text_to_be_typed):
        web_element = self.get_element(locator_type, element)

        if self.wait_for_element(web_element):
            self.driver.execute_script("arguments[0].value = arguments[1];", web_element, text_to_be_typed)
            self.logger.info(f"Entered text '{text_to_be_typed}' in the element using JavaScriptExecutor")

        else:
            logging.error("javascript_type() trigger >>> SEEMS element is not available in dom ", element)

    def get_element_text(self, locator_type, element):
        text = None
        web_element = self.get_element(locator_type, element)

        if self.wait_for_element(web_element):
            text = web_element.text
        else:
            logging.error("get_element_text() trigger >>> SEEMS element is not available in dom ", element)

        return text

    def is_element_displayed(self, locator_type, element):
        web_element = self.get_element(locator_type, element)
        try:
            if self.wait_for_element(web_element):
                return web_element.is_displayed()
            else:
                logging.error("is_element_displayed() trigger >>> SEEMS element is not available in dom ", element)
        except Exception as e:
            self.logger.error(f"Error checking element display: {e}")
            print("Getting some Error")
            return False

    def is_element_selected(self, web_element):

        try:
            if self.wait_for_element(web_element):
                return web_element.is_checked()
            else:
                logging.error("click_element() trigger >>> SEEMS element is not available in dom ", web_element)

        except Exception as e:
            self.logger.error(f"Error checking element display: {e}")
            print("Getting some Error")
            return False

    def select_check_box_or_radio_button(self, locator_type, element):
        element = self.get_element(locator_type, element)
        if not self.is_element_selected(element):
            element.click()

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_current_url(self):
        return self.driver.current_url
