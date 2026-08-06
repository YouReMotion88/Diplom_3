from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderPage(BasePage):

    def click_constructor(self):
        self.click_element(
            HeaderLocators.CONSTRUCTOR_BUTTON
        )

    def click_order_feed(self):
        self.click_element(
            HeaderLocators.ORDER_FEED_BUTTON
        )