from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_target(context):
    context.driver.get('https://target.com/')
    sleep(4)


@when('Search for {item}')
def search_for_item(context, item):
    context.driver.find_element(By.ID, 'search').send_keys(f'{item}')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)


@when('Click on Target Circle')
def click_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


@when('Click on Sign in button')
def main_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink'] span").click()
    sleep(4)


@when('Click on Sign in in navigation panel')
def navigational_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn'] span").click()
    sleep(4)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()
    sleep(4)