from selenium.webdriver.common.by import By

class BrowserWindowsPageLocators:
    """
    Locators for the page https://demoqa.com/browser-windows
    """

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
