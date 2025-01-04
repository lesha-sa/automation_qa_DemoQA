from selenium.webdriver.common.by import By

class DynamicPropertiesPageLocators:
    """
    Locators for the page https://demoqa.com/dynamic-properties
    """
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')