from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when("Click 'Add to cart' on the first item")
def add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper'] [data-test='chooseOptionsButton']"))).click()


@when("Click 'Add to cart' button on the navigational panel")
def add_to_cart_navigational(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='orderPickupButton']"))).click()


@when("Click 'View cart & check out' button")
def view_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/cart']"))).click()




