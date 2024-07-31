from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.base_page import Page


@given('Open Help page for Returns')
def open_help_returns(context):
    context.app.help_page.open_help_returns_page()


@when('Select Help topic Delivery & Pickup')
def select_topic(context):
    context.app.help_page.select_delivery_and_pickup()


@then('Verify help Returns page opened')
def verify_help_returns_opened(context):
    context.app.help_page.verify_help_returns_page()


@then('Verify help Delivery & Pickup page opened')
def verify_selected_topic(context):
    context.app.help_page.verify_delivery_and_pickup_opened()

