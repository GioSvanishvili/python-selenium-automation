from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

from time import sleep


class LogInPage(Page):

    LOG_IN_PAGE_TXT = (By.XPATH, "//span[text()='Sign into your Target account']")
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login')
    LOGGED_IN_UESRS_NAME = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    TC_LINK_BTN = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")
    LOG_IN_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='authAlertDisplay'] div")

    def open_log_in_page(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def verify_sign_in_page(self):
        actual_result = self.driver.find_element(*self.LOG_IN_PAGE_TXT).text
        assert 'Sign into your Target account' in actual_result, f"Expected 'Sign into your Target account' but got'{actual_result}'"

    def type_email(self, text):
        self.input_text(text, *self.EMAIL_FIELD)

    def type_incorrect_email(self, text):
        self.input_text(text, *self.EMAIL_FIELD)

    def type_password(self, text):
        self.input_text(text, *self.PASSWORD_FIELD)

    def type_incorrect_password(self, text):
        self.input_text(text, *self.PASSWORD_FIELD)

    def login(self):
        self.click(*self.LOGIN_BTN)

    def click_tc(self):
        self.wait_and_click(*self.TC_LINK_BTN)

    def verify_log_in_successful(self):
        sleep(6)
        users_name = self.driver.find_element(*self.LOGGED_IN_UESRS_NAME).text
        assert 'testname' in users_name, f"Expected 'testname' but got'{users_name}'"

    def verify_error_log_in_message(self):
        self.wait_for_element_appear(self.LOG_IN_ERROR_MESSAGE)
        self.verify_text("We can't find your account.", *self.LOG_IN_ERROR_MESSAGE)
