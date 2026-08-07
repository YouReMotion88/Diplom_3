import allure
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class FeedPage(BasePage):

    @allure.step("Получить общее количество заказов")
    def get_total_orders(self):
        return int(
            self.get_text(
                FeedLocators.TOTAL_ORDERS
            )
        )


    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return int(
            self.get_text(
                FeedLocators.TODAY_ORDERS
            )
        )


    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.wait_loading_disappears()
        self.click_element(
            FeedLocators.FEED_BUTTON
        )


    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click_element(
            FeedLocators.CONSTRUCTOR_BUTTON
        )


    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self):
        for _ in range(3):
            try:
                elements = self.wait.until(
                    EC.visibility_of_all_elements_located(
                        FeedLocators.IN_PROGRESS_ORDER
                    )
                )
                return [element.text for element in elements]
            except StaleElementReferenceException:
                pass

        raise StaleElementReferenceException(
            "Не удалось получить список заказов в работе"
        )


    @allure.step("Дождаться загрузки ленты заказов")
    def wait_feed_loaded(self):
        self.find_element(
            FeedLocators.FEED_TITLE
        )