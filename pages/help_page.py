from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

from pages.base_page import Page


class HelpPage(Page):

    HELP_RETURNS_TITLE = (By.XPATH, "//div[@class='container_24'] //h1[text()=' Returns']")
    HELP_DELIVERY_AND_PICKUP_TITLE = (By.CSS_SELECTOR, ".leftNavLinkDiv h2")
    MENU = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")

    def open_help_returns_page(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_delivery_and_pickup(self):
        dropdown_menu = self.find_element(*self.MENU)
        select = Select(dropdown_menu)
        select.select_by_value('Delivery & Pickup')

    def verify_help_returns_page(self):
        self.verify_text('Returns', *self.HELP_RETURNS_TITLE)

    def verify_delivery_and_pickup_opened(self):
        self.verify_text('Delivery & Pickup', *self.HELP_DELIVERY_AND_PICKUP_TITLE)
