from selenium.webdriver.common.by import By


class FeedLocators:

    # Кнопка "Лента заказов"
    FEED_BUTTON = (
        By.XPATH,
        "//a[p[text()='Лента Заказов']]"
    )

    # Выполнено за всё время
    TOTAL_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    # Выполнено за сегодня
    TODAY_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    IN_PROGRESS_TITLE = (
        By.XPATH,
        "//p[text()='В работе:']"
    )

    # Заказы в работе
    IN_PROGRESS_ORDER = (
    By.XPATH,
    "//p[text()='В работе:']/following-sibling::ul//li"
)

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[p[text()='Конструктор']]"
    )