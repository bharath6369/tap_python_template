import time

from behave import *

from features.page.SignUpPage import SignUpPage

from utils.CommonUtils import CommonUtils


@When("the user clicks on the SignIn link located on the SignUp page")
def step_impl(context):
    time.sleep(3)
    context.sign_up_page = SignUpPage(context.driver)
    context.sign_in_page = context.sign_up_page.click_on_sign_in_link()


@then("the user should be redirected to the SignIn page")
def step_impl(context):
    assert context.sign_in_page.check_is_sign_in_page_loaded()


@when(u'the user enters "{Email}" in the email address field')
def step_impl(context, Email):
    context.sign_in_page.enter_email_address(Email)


@when('the user enters "{Password}" in the password field')
def step_impl(context, Password):
    context.sign_in_page.enter_password(Password)


# @when(u'the user enters "kashishrajput694@gmail.com" in the email address field')
# def step_impl(context):
#     print("hello", context.Email)
@when('the user clicks the SignIn button')
def step_impl(context):
    context.sign_in_page.click_on_login_button()


@Then('user should able to see "{email_error}" error message for email')
def step_impl(context, email_error):
    assert context.sign_in_page.email_mandatory_field_missing_text() == email_error


@Then('user should able to see "{password_error}" error message for password')
def step_impl(context, password_error):
    assert context.sign_in_page.password_mandatory_field_missing_text() == password_error

