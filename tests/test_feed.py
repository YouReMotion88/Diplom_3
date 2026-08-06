import allure

from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


@allure.title("После создания заказа увеличивается счётчик за всё время")
def test_total_orders_increases(
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

    with allure.step("Запоминаем количество заказов"):
        feed.open_feed()
        before = feed.get_total_orders()

    with allure.step("Переходим в конструктор"):
        feed.open_constructor()

    with allure.step("Создаем заказ"):
        constructor.drag_ingredient_to_constructor()
        constructor.click_order_button()

    with allure.step("Получаем номер заказа"):
        order_number = constructor.wait_order_number()

    with allure.step("Проверяем увеличение счетчика"):
        assert order_number == before + 1


@allure.title("После создания заказа увеличивается счётчик за сегодня")
def test_today_orders_increases(
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

    with allure.step("Переходим в конструктор"):
        feed.open_constructor()

    with allure.step("Создаем заказ"):
        constructor.drag_ingredient_to_constructor()
        constructor.click_order_button()
        constructor.wait_order_number()

    with allure.step("Закрываем окно заказа"):
        constructor.close_order_modal()

    with allure.step("Переходим в ленту заказов"):
        feed.open_feed()
        after = feed.get_today_orders()

    with allure.step("Проверяем увеличение счетчика"):
        assert after == before + 1


@allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
def test_order_appears_in_progress(
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

    with allure.step("Переходим в конструктор"):
        feed.open_constructor()

    with allure.step("Создаем заказ"):
        constructor.drag_ingredient_to_constructor()
        constructor.click_order_button()

    with allure.step("Получаем номер заказа"):
        order_number = constructor.wait_order_number()

    with allure.step("Закрываем модальное окно"):
        constructor.close_order_modal()

    with allure.step("Переходим в ленту заказов"):
        feed.open_feed()

    with allure.step("Получаем список заказов в работе"):
        orders = feed.get_orders_in_progress()

        print(order_number)
        print(orders)

    with allure.step("Проверяем, что заказ появился в работе"):
        assert f"0{order_number}" in orders