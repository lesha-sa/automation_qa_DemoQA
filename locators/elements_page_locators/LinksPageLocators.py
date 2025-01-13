from selenium.webdriver.common.by import By


class LinksPageLocators:
    """
    Locators for the page https://demoqa.com/radio-button
    """
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")