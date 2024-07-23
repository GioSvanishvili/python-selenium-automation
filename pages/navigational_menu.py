from selenium.webdriver.common.by import By
from pages.base_page import Page


class NavigationMenu(Page):

    NAVIGATIONAL_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn'] span")
    NAVIGATIONAL_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    NAVIGATIONAL_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")

    def navigational_sign_in(self):
        self.click(*self.NAVIGATIONAL_SIGN_IN)

    def navigational_add_to_cart(self):
        self.click(*self.NAVIGATIONAL_ADD_TO_CART_BTN)

    def navigational_view_cart(self):
        self.click(*self.NAVIGATIONAL_VIEW_CART_BTN)

