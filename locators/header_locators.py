from selenium.webdriver.common.by import By


class HeaderLocators:

    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[@href='/']"
    )


    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//a[@href='/feed']"
    )

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        ".Modal_modal_overlay__x2ZCr"
    )