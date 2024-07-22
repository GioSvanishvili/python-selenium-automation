from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@given('Open target.com')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_for_item(context, product):
    context.app.header.search_product(product)


@when('Click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


@when('Click on Sign in button')
def main_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/AccountLink'] span"))).click()


@when('Click on Sign in in navigation panel')
def navigational_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn'] span"))).click()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']"))).click()
