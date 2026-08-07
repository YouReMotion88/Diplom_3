import allure

from pages.header_page import HeaderPage
from pages.constructor_page import ConstructorPage
from urls import HOME_PAGE, FEED_PAGE
from pages.feed_page import FeedPage

class TestConstructor:

    @allure.title("Переход в конструктор по кнопке «Конструктор»")
    def test_open_constructor(self, driver):

        header = HeaderPage(driver)
        feed = FeedPage(driver)

        with allure.step("Открываем страницу Ленты заказов"):
            driver.get(FEED_PAGE)
            feed.wait_feed_loaded()
            
        with allure.step("Переходим в конструктор"):
            header.click_constructor()
        
        
        assert driver.current_url == HOME_PAGE
                

    @allure.title("Переход в Ленту заказов по кнопке «Лента заказов»")
    def test_open_order_feed(self, driver):

        with allure.step("Открываем главную страницу"):
            driver.get(HOME_PAGE)
                
        header = HeaderPage(driver)

        with allure.step("Нажимаем кнопку Лента заказов"):
            header.click_order_feed()

        assert driver.current_url == FEED_PAGE
                

    @allure.title("При клике на ингредиент открывается окно с деталями")
    def test_open_ingredient_modal(self, driver):

        driver.get(HOME_PAGE)

        constructor = ConstructorPage(driver)

        with allure.step("Открываем окно деталей ингредиента"):
            constructor.click_ingredient()
        
        assert constructor.is_modal_open()


    @allure.title("Окно деталей ингредиента закрывается по клику на крестик")
    def test_close_ingredient_modal(self, driver):

        driver.get(HOME_PAGE)

        constructor = ConstructorPage(driver)

        with allure.step("Открываем и закрываем окно деталей"):
            constructor.click_ingredient()
            constructor.close_modal()

        assert constructor.is_modal_closed()


    @allure.title("Счётчик ингредиента увеличивается после добавления в заказ")
    def test_ingredient_counter_increases(self, driver):
        driver.get(HOME_PAGE)

        constructor = ConstructorPage(driver)
       
        counter_before = constructor.get_counter_value()

        with allure.step("Добавляем ингредиент в конструктор"):
            constructor.drag_ingredient_to_constructor()

        counter_after = constructor.get_counter_value()

        assert counter_after > counter_before
    