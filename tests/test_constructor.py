import time
import allure

from pages.header_page import HeaderPage
from pages.constructor_page import ConstructorPage
from urls import HOME_PAGE, FEED_PAGE


class TestConstructor:

    @allure.title("Переход в конструктор по кнопке «Конструктор»")
    def test_open_constructor(self, driver):

        with allure.step("Открываем страницу Ленты заказов"):
            driver.get(FEED_PAGE)

            time.sleep(1)

            header = HeaderPage(driver)

        with allure.step("Нажимаем кнопку Конструктор"):
            header.click_constructor()

        with allure.step("Проверяем переход на страницу конструктора"):
            assert driver.current_url == HOME_PAGE
                

    @allure.title("Переход в Ленту заказов по кнопке «Лента заказов»")
    def test_open_order_feed(self, driver):

        with allure.step("Открываем главную страницу"):
            driver.get(HOME_PAGE)
                
        header = HeaderPage(driver)

        with allure.step("Нажимаем кнопку Лента заказов"):
            header.click_order_feed()

        with allure.step("Проверяем переход в Ленту заказов"):
            assert driver.current_url == FEED_PAGE
                

    @allure.title("При клике на ингредиент открывается окно с деталями")
    def test_open_ingredient_modal(self, driver):

        with allure.step("Открываем главную страницу"):
            driver.get(HOME_PAGE)

        constructor = ConstructorPage(driver)

        with allure.step("Нажимаем на ингредиент"):
            constructor.click_ingredient()

        with allure.step("Проверяем, что открылось окно с деталями"):
            assert constructor.is_modal_open()


    @allure.title("Окно деталей ингредиента закрывается по клику на крестик")
    def test_close_ingredient_modal(self, driver):

        with allure.step("Открываем главную страницу"):
            driver.get(HOME_PAGE)

        constructor = ConstructorPage(driver)

        with allure.step("Открываем окно деталей ингредиента"):
            constructor.click_ingredient()

        with allure.step("Закрываем окно"):
            constructor.close_modal()

        with allure.step("Проверяем, что окно закрылось"):
            assert constructor.is_modal_closed()


    @allure.title("Счётчик ингредиента увеличивается после добавления в заказ")
    def test_ingredient_counter_increases(self, driver):

        with allure.step("Открываем главную страницу"):
            driver.get(HOME_PAGE)

            constructor = ConstructorPage(driver)

        with allure.step("Получаем начальное значение счётчика ингредиента"):
            counter_before = constructor.get_counter_value()

        with allure.step("Добавляем ингредиент в конструктор"):
            constructor.drag_ingredient_to_constructor()

        with allure.step("Получаем значение счётчика после добавления ингредиента"):
            counter_after = constructor.get_counter_value()

        with allure.step("Проверяем, что счётчик ингредиента увеличился"):
            assert counter_after > counter_before
    