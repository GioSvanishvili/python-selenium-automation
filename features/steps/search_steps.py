from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click 'Add to cart' on the first item")
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper'] [data-test='chooseOptionsButton']").click()
    sleep(3)


@when("Click 'Add to cart' button on the navigational panel")
def add_to_cart_navigational(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(3)


@when("Click 'View cart & check out' button")
def view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()
    sleep(5)




