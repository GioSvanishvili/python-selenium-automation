from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Type the email address')
def type_email(context):
    context.app.log_in_page.type_email('bjy2000@monshua.com')


@when('Type the password')
def type_password(context):
    context.app.log_in_page.type_password('************')


@when('Sign in with password')
def log_in(context):
    context.app.log_in_page.login()


@then('Verify log in was successful')
def verify_log_in_successful(context):
    context.app.log_in_page.verify_log_in_successful()


@then('Verify log in page')
def verify_log_in(context):
    context.app.log_in_page.verify_sign_in_page()


