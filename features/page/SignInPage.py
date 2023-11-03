import time

from utils.ElementUtils import ElementUtils


class SignInPage(ElementUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.warning_message_xpath = None

    signInLink_xpath = "//a[contains(text(),' Sign in')]"
    emailAddressField_id = "email"
    passwordField_id = "password"
    signInButton_xpath = "//*[@type='submit']"
    quickSurveyPage_id = "quickSurveyPage"
    email_mandatory_field_missing_css = "p[id='email-helper-text']"
    password_mandatory_field_missing_css = "p[id='password-helper-text']"

    def click_on_login_link(self):
        self.clear_element('signInLink_xpath', self.signInLink_xpath)

    def enter_email_address(self, email_text):
        self.clear_and_send_keys('emailAddressField_id', self.emailAddressField_id, email_text)

    def enter_password(self, password_text):
        self.clear_and_send_keys('passwordField_id', self.passwordField_id, password_text)

    def click_on_login_button(self):
        self.click_element('signInButton_xpath', self.signInButton_xpath)
        # need to return the page

    def check_is_sign_in_page_loaded(self):

        # print('++++++++++++++++++++++++++++',
        #       self.is_element_displayed('emailAddressField_id', self.emailAddressField_id))
        # self.clear_and_send_keys('emailAddressField_id', self.emailAddressField_id, "hello")

        if (self.is_element_displayed('emailAddressField_id', self.emailAddressField_id)
                and self.is_element_displayed('passwordField_id', self.passwordField_id)
                and self.is_element_displayed('signInButton_xpath', self.signInButton_xpath)):
            result = True
        else:
            result = False

        return result

    def email_mandatory_field_missing_text(self):
        return self.get_element_text('email_mandatory_field_missing_css', self.email_mandatory_field_missing_css)

    def password_mandatory_field_missing_text(self):
        return self.get_element_text('password_mandatory_field_missing_css', self.password_mandatory_field_missing_css)
