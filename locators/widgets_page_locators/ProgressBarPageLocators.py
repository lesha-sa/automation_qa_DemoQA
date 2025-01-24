from selenium.webdriver.common.by import By


class ProgressBarPageLocators:
    """
    Locators for the page https://demoqa.com/progress_bar
    """
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR,'div[class="progress-bar bg-info"]')