from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться исчезновения модального оверлея")
    def wait_loading_disappears(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                HeaderLocators.MODAL_OVERLAY
            )
        )

    @allure.step("Выполнить скрипт JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
