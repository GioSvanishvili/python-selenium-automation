from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_TXT = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")
    ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test='cart-order-summary'] div span")

    def verify_text(self):
        actual_message = self.driver.find_element(*self.CART_EMPTY_TXT).text
        assert 'Your cart is empty' in actual_message, f"Expected 'Your cart is empty' but got {actual_message}"

    def verify_item_in_cart(self, cart_amount):
        item_in_cart = self.driver.find_element(*self.ITEM_IN_CART).text
        assert item_in_cart in cart_amount, f'Expected {cart_amount} but got {item_in_cart}'
