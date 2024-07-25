from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.log_in_page.open_log_in_page()


@given('Store original window')
def store_og_window(context):
    context.og_window = context.app.log_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.log_in_page.click_tc()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.log_in_page.switch_to_new_window()


@when('User can close new window and switch back to original')
def close_new_window(context):
    context.app.log_in_page.close()


@when('Type the email address')
def type_email(context):
    context.app.log_in_page.type_email('bjy2000@monshua.com')


@when('Type the password')
def type_password(context):
    context.app.log_in_page.type_password('************')


@when('Sign in with password')
def log_in(context):
    context.app.log_in_page.login()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_and_conditions_page.verify_tc_opened()


@then('Verify log in was successful')
def verify_log_in_successful(context):
    context.app.log_in_page.verify_log_in_successful()


@then('Verify log in page')
def verify_log_in(context):
    context.app.log_in_page.verify_sign_in_page()


