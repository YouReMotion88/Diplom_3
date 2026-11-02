from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class HeaderPage(BasePage):

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click_element(
            HeaderLocators.CONSTRUCTOR_BUTTON
        )


    @allure.step("Перейти в ленту заказов")
    def click_order_feed(self):
        self.click_element(
            HeaderLocators.ORDER_FEED_BUTTON
        )


    @allure.step("Дождаться доступности кнопки «Конструктор»")
    def wait_constructor_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                HeaderLocators.CONSTRUCTOR_BUTTON
            )
        )
        