from selenium.webdriver.common.by import By


class ModalDialogsPageLocators:
    """
    Locators for the page https://demoqa.com/modal-dialogs
    """
    SMALL_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    SMALL_MODEL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    SMALL_MODEL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    SMALL_MODEL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    LARGE_MODEL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    LARGE_MODEL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    LARGE_MODEL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    LARGE_MODEL_TITLE = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")



