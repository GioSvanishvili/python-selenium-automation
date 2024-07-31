from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from pages.navigational_menu import NavigationMenu
from pages.log_in_page import LogInPage
from pages.terms_and_conditions_page import TermsAndConditionsPage
from pages.help_page import HelpPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.navigational_menu = NavigationMenu(driver)
        self.log_in_page = LogInPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.help_page = HelpPage(driver)
