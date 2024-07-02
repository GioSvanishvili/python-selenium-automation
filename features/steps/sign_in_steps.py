from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign in button')
def main_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink'] span").click()
    sleep(4)


@when('Click on Sign in in navigation panel')
def navigational_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn'] span").click()
    sleep(4)


@then('Verify log in page')
def verify_log_in(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Expected "{expected_result}" but got "{actual_result}"'
