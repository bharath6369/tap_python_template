import pdb
import time

from behave import *

from features.page.SignInPage import SignInPage
from features.page.SignUpPage import SignUpPage
from utils.CommonUtils import CommonUtils


@given(u'the user is on the Sign Up Page')
def step_impl(context):
    context.sign_up_page = SignUpPage(context.driver)
    context.sign_in_page = SignInPage(context.driver)
    time.sleep(3)


@Then('the user should be redirected to the signup page')
def step_impl(context):
    assert context.sign_up_page.check_sign_up_page_loaded()


@when(u'the user enters "{first_name}" into the First Name field')
def step_impl(context, first_name):
    context.sign_up_page.enter_first_name(first_name)


@when(u'the user enters "{last_name}" into the Last Name field')
def step_impl(context, last_name):
    context.sign_up_page.enter_last_name(last_name)


@when(u'I enter random email in the email address field')
def step_impl(context):
    email = CommonUtils.get_email_with_time_stamp()

    context.sign_up_page.enter_email_address(email)


@when('the user enters "{password}" in the password field in signup page')
def step_impl(context, password):
    context.sign_up_page.enter_password_field(password)


@when(u'the user selects the Terms and Conditions checkbox')
def step_impl(context):
    context.sign_up_page.select_term_condition()


@when(u'user clicks on the Sign up button')
def step_impl(context):
    context.confirm_email_page = context.sign_up_page.click_on_sign_up_button()


@then(u'the user should be redirected to the Confirm Email Page')
def step_impl(context):
    assert context.confirm_email_page.check_confirm_email_page_redirection()


@then(u'user should able to see "{first_error_message}" error message for firstname')
def step_impl(context, first_error_message):
    assert context.sign_up_page.first_name_mandatory_field_missing_text() == first_error_message


@then(u'user should able to see "{last_name_error_message}" error message for lastname')
def step_impl(context, last_name_error_message):
    assert context.sign_up_page.last_name_mandatory_field_missing_text() == last_name_error_message


@then(u'user should able to see "{term_related_error_message}" for terms and conditions')
def step_impl(context, term_related_error_message):
    assert context.sign_up_page.term_condition_mandatory_field_missing_text() == term_related_error_message


@when(u'user should able to see "{invalid_email}" error message for email')
def step_impl(context, invalid_email):
    assert context.sign_up_page.invalid_email_message() == invalid_email


@when(u'I enter "{used_email}" that is already in use in the email address field')
def step_impl(context, used_email):
    context.sign_up_page.enter_email_address(used_email)


@then(u'I should see an error message that the email is already in use')
def step_impl(context):
    assert "already exist" in context.sign_up_page.get_message_email_already_in_use()
