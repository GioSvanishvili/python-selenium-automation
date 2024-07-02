from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://target.com/')
    sleep(4)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()
    sleep(4)


@then('Verify Your cart is empty is shown')
def verify_cart_is_empty(context):
    expected_message = 'Your cart is empty'
    actual_message = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    assert expected_message in actual_message, f'Expected {expected_message} but got {actual_message}'
