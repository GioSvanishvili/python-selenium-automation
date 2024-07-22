from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_TXT = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")

    def verify_text(self):
        actual_message = self.driver.find_element(*self.CART_EMPTY_TXT).text
        assert 'Your cart is empty' in actual_message, f"Expected 'Your cart is empty' but got {actual_message}"
