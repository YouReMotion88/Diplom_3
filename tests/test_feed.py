import allure

from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


class TestFeed:
    @allure.title("После создания заказа увеличивается счётчик за всё время")
    def test_total_orders_increases(
        self,
        driver,
        registered_user
    ):
        email, password = registered_user

        login = LoginPage(driver)
        constructor = ConstructorPage(driver)
        feed = FeedPage(driver)

        with allure.step("Авторизуемся"):
            login.open_login_page()
            login.login(email, password)

        with allure.step("Запоминаем текущее количество заказов"):
            feed.open_feed()
            before = feed.get_total_orders()

        with allure.step("Создаем заказ"):
            feed.open_constructor()
            constructor.drag_ingredient_to_constructor()
            constructor.click_order_button()
       
        order_number = constructor.wait_order_number()
    
        assert order_number == before + 1


    @allure.title("После создания заказа увеличивается счётчик за сегодня")
    def test_today_orders_increases(
        self,
        driver,
        registered_user
    ):
        email, password = registered_user

        login = LoginPage(driver)
        constructor = ConstructorPage(driver)
        feed = FeedPage(driver)

        with allure.step("Авторизуемся"):
            login.open_login_page()
            login.login(email, password)

        with allure.step("Запоминаем количество заказов за сегодня"):
            feed.open_feed()
            before = feed.get_today_orders()

        with allure.step("Создаем заказ"):
            feed.open_constructor()
            constructor.drag_ingredient_to_constructor()
            constructor.click_order_button()
            constructor.wait_order_number()

        with allure.step("Проверяем количество заказов после оформления"):
            constructor.close_order_modal()
            feed.open_feed()
            after = feed.get_today_orders()

        assert after == before + 1


    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(
        self,
        driver,
        registered_user
    ):
        email, password = registered_user

        login = LoginPage(driver)
        constructor = ConstructorPage(driver)
        feed = FeedPage(driver)

        with allure.step("Авторизуемся"):
            login.open_login_page()
            login.login(email, password)

        with allure.step("Создаем заказ"):
            feed.open_constructor()
            constructor.drag_ingredient_to_constructor()
            constructor.click_order_button()
        
        order_number = constructor.wait_order_number()

        with allure.step("Проверяем заказ в разделе «В работе»"):
            constructor.close_order_modal()
            feed.open_feed()
            orders = feed.get_orders_in_progress()
       
        assert f"0{order_number}" in orders