from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import LOGIN_PAGE, HOME_PAGE
import time
from selenium.webdriver.support import expected_conditions as EC
import allure



class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find_element(
            LoginLocators.EMAIL_INPUT
        ).send_keys(email)


    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.find_element(
            LoginLocators.PASSWORD_INPUT
        ).send_keys(password)


    @allure.step("Нажать кнопку «Войти»")
    def click_login(self):

        time.sleep(0.3)
        
        self.click_element(
            LoginLocators.LOGIN_BUTTON
        )


    @allure.step("Авторизоваться")
    def login(self, email, password):
        
        self.enter_email(email)
        self.enter_password(password)

        self.click_login()
        self.wait_home_page_opened()
        

    @allure.step("Дождаться открытия главной страницы")
    def wait_home_page_opened(self):
        self.wait.until(
            EC.url_to_be(HOME_PAGE)
        )


    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open(LOGIN_PAGE)