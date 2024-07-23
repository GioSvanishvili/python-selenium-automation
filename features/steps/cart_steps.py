from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Your cart is empty is shown')
def verify_cart_is_empty(context):
    expected_message = 'Your cart is empty'
    actual_message = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1").text
    assert expected_message in actual_message, f'Expected {expected_message} but got {actual_message}'


@then('Verify {cart_amount} item is in cart')
def verify_items_in_cart(context, cart_amount):
    context.app.cart_page.verify_item_in_cart(cart_amount)



