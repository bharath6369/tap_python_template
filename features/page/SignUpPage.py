import time

from features.page.ConfirmEmailPage import ConfirmEmailPage
from features.page.SignInPage import SignInPage
from utils.ElementUtils import ElementUtils


class SignUpPage(ElementUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.warning_message_xpath = None

    sign_in_link_css = "a[href*='signin']"
    first_name_id = "firstName"
    last_name_id = "lastName"
    email_field_id = "email"
    password_field_id = "password"
    term_condition_css = "input[type='checkbox']"
    sign_up_button_css = "button[type='submit']"
    first_name_error_id = "firstName-helper-text"
    last_name_error_id = "lastName-helper-text"
    term_condition_css_error_css = "div [class*='MuiBox']+p[class*='css']"
    email_invalid_mess_id = "email-helper-text"
    email_already_in_use_xpath = "//div[contains(text(),'already exists')]"

    # def return_signup_page(self):
    #     return SignUpPage(self.driver)

    def check_sign_up_page_loaded(self):
        if (self.is_element_displayed('first_name_id', self.first_name_id)
                and self.is_element_displayed('last_name_id', self.last_name_id)
                and self.is_element_displayed('email_field_id', self.email_field_id)
                and self.is_element_displayed('password_field_id', self.password_field_id)
                and self.is_element_displayed('term_condition_css', self.term_condition_css)
                and self.is_element_displayed('sign_up_button_css', self.sign_up_button_css)):
            result = True
        else:
            result = False

        return result

    def enter_first_name(self, first_name):
        self.clear_and_send_keys('first_name_id', self.first_name_id, first_name)

    def enter_last_name(self, last_name):
        self.clear_and_send_keys('last_name_id', self.last_name_id, last_name)

    def enter_email_address(self, email_field):
        self.clear_and_send_keys('email_field_id', self.email_field_id, email_field)

    def enter_password_field(self, password_field):
        self.clear_and_send_keys('password_field_id', self.password_field_id, password_field)

    def select_term_condition(self):
        self.select_check_box_or_radio_button('term_condition_css', self.term_condition_css)

    def first_name_mandatory_field_missing_text(self):
        return self.get_element_text('first_name_error_id', self.first_name_error_id)

    def last_name_mandatory_field_missing_text(self):
        return self.get_element_text('last_name_error_id', self.last_name_error_id)

    def term_condition_mandatory_field_missing_text(self):
        return self.get_element_text('term_condition_css_error_css', self.term_condition_css_error_css)

    def invalid_email_message(self):
        return self.get_element_text('invalid_email_message', self.invalid_email_message())

    def get_message_email_already_in_use(self):
        time.sleep(2)
        return self.get_element_text('email_already_in_use_xpath', self.email_already_in_use_xpath)

    def click_on_sign_up_button(self):
        self.click_element('sign_up_button_css', self.sign_up_button_css)
        return ConfirmEmailPage(self.driver)

    def click_on_sign_in_link(self):
        self.click_element('sign_in_link_css', self.sign_in_link_css)
        return SignInPage(self.driver)
