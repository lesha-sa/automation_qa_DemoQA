from selenium.webdriver.common.by import By


class MenuPageLocators:
    """
    Locators for the page https://demoqa.com/menu
    """
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')