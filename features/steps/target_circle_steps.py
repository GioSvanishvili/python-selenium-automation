from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify all {link_amount} links')
def verify_link_amount(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, ".cell-item-content")
    assert len(links) == link_amount, f'Expected {link_amount} links, got {len(links)}'


