from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.common.exceptions import ElementClickInterceptedException


class ConstructorPage(BasePage):

    @allure.step("Кликнуть по ингредиенту")
    def click_ingredient(self):
        self.wait_loading_disappears()

        self.click_element(
            ConstructorLocators.INGREDIENT
        )


    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_open(self):
        return self.find_element(
            ConstructorLocators.INGREDIENT_MODAL
        )


    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_element(
            ConstructorLocators.CLOSE_MODAL_BUTTON
        )


    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                ConstructorLocators.INGREDIENT_MODAL
            )
        )


    @allure.step("Получить значение счётчика ингредиента")
    def get_counter_value(self):
        return int(
            self.get_text(
                ConstructorLocators.INGREDIENT_COUNTER
            )
        )


    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element(
            ConstructorLocators.INGREDIENT
        )

        constructor = self.find_element(
            ConstructorLocators.CONSTRUCTOR_DROP_AREA
        )

        self.execute_script("""
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) {
                        this.data[key] = value;
                    },
                    getData: function(key) {
                        return this.data[key];
                    }
                };
                return event;
            }

            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                element.dispatchEvent(event);
            }

            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(arguments[0], dragStartEvent);

            var dropEvent = createEvent('drop');
            dispatchEvent(arguments[1], dropEvent, dragStartEvent.dataTransfer);

            var dragEndEvent = createEvent('dragend');
            dispatchEvent(arguments[0], dragEndEvent, dropEvent.dataTransfer);

        """, ingredient, constructor)

        self.wait.until(
            lambda driver: self.get_counter_value() == 2
        )

    @allure.step("Нажать кнопку «Оформить заказ»")
    def click_order_button(self):
        self.click_element(
            ConstructorLocators.ORDER_BUTTON
        )


    @allure.step("Закрыть окно оформления заказа")
    def close_order_modal(self):
        # Сначала пробую обычный клик
        try:
            self.click_element(ConstructorLocators.CLOSE_MODAL_BUTTON)
        except ElementClickInterceptedException:
            # Если не получилось — кликаюю через JS
            close_button = self.find_element(ConstructorLocators.CLOSE_MODAL_BUTTON)
            self.execute_script("arguments[0].click();", close_button)
        
        self.wait.until(
            EC.invisibility_of_element_located(ConstructorLocators.ORDER_NUMBER)
        )


    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return int(
            self.get_text(
                ConstructorLocators.ORDER_NUMBER
            )
        )


    @allure.step("Дождаться отображения номера заказа")
    def wait_order_number(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_order_number() != 9999
        )

        return self.get_order_number()