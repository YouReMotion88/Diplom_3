from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ConstructorPage(BasePage):

    def click_ingredient(self):
        self.wait_loading_disappears()

        self.click_element(
            ConstructorLocators.INGREDIENT
        )

    def is_modal_open(self):
        return self.find_element(
            ConstructorLocators.INGREDIENT_MODAL
        )

    def close_modal(self):
        self.click_element(
            ConstructorLocators.CLOSE_MODAL_BUTTON
        )

    def is_modal_closed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                ConstructorLocators.INGREDIENT_MODAL
            )
        )


    def get_counter_value(self):
        return int(
            self.get_text(
                ConstructorLocators.INGREDIENT_COUNTER
            )
        )


    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element(
            ConstructorLocators.INGREDIENT
        )

        constructor = self.find_element(
            ConstructorLocators.CONSTRUCTOR_DROP_AREA
        )

        self.driver.execute_script("""
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


    def click_order_button(self):
        self.click_element(
            ConstructorLocators.ORDER_BUTTON
        )


    def wait_order_number(self):
        self.find_element(
            ConstructorLocators.ORDER_NUMBER
        )


    def close_order_modal(self):
        import time
        time.sleep(1)
        self.click_element(
            ConstructorLocators.CLOSE_MODAL_BUTTON
        )


    def get_order_number(self):
        return int(
            self.get_text(
                ConstructorLocators.ORDER_NUMBER
            )
        )


    def wait_order_number(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_order_number() != 9999
        )

        return self.get_order_number()