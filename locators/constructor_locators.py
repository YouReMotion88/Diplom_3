from selenium.webdriver.common.by import By


class ConstructorLocators:

    # Карточка ингредиента
    INGREDIENT = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']/ancestor::a"
    )

    # Заголовок модального окна
    INGREDIENT_MODAL = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']"
    )


    INGREDIENT_COUNTER = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']/ancestor::a//div[contains(@class,'counter')]//p"
    )

    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        "//span[text()='Перетяните булочку сюда (верх)']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    FIRST_BUN = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a"
    )

    FIRST_SAUCE = (
        By.XPATH,
        "//p[text()='Соус Spicy-X']/ancestor::a"
    )

    FIRST_FILLING = (
        By.XPATH,
        "//p[text()='Мясо бессмертных моллюсков Protostomia']/ancestor::a"
    )

    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        ".Modal_modal__title_shadow__3ikwq"
    )

    CLOSE_MODAL_BUTTON = (
        By.CSS_SELECTOR,
        "button.Modal_modal__close__TnseK"
    )