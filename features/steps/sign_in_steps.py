from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify log in page')
def verify_log_in(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Expected "{expected_result}" but got "{actual_result}"'
