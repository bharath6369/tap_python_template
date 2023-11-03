import time

from utils.ElementUtils import ElementUtils


class ConfirmEmailPage(ElementUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.warning_message_xpath = None

    confirm_email_page_xpath = "//h2[text()='Confirm your email']"

    def check_confirm_email_page_redirection(self):
        time.sleep(10)
        actual_msg = self.get_element_text('confirm_email_page_xpath', self.confirm_email_page_xpath)
        expected_msg = 'Confirm your email'
        expected_url = 'email-verification-sent'
        if (expected_msg in actual_msg and
                expected_url in self.get_current_url()):
            return True

        else:
            return False
