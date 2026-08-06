from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import LOGIN_PAGE, HOME_PAGE
import time
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    def enter_email(self, email):
        self.find_element(
            LoginLocators.EMAIL_INPUT
        ).send_keys(email)

    def enter_password(self, password):
        self.find_element(
            LoginLocators.PASSWORD_INPUT
        ).send_keys(password)

    def click_login(self):
        time.sleep(1)
        self.click_element(
            LoginLocators.LOGIN_BUTTON
        )

    def login(self, email, password):
        
        self.enter_email(email)
        self.enter_password(password)

        self.click_login()
        self.wait_home_page_opened()

    def wait_home_page_opened(self):
        self.wait.until(
            EC.url_to_be(HOME_PAGE)
        )

    def open_login_page(self):
        self.open(LOGIN_PAGE)