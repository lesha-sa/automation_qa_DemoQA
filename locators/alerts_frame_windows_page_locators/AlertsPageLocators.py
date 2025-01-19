from selenium.webdriver.common.by import By


class AlertsPageLocators:
    """
    Locators for the page https://demoqa.com/alerts
    """
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMT_RESULT = (By.CSS_SELECTOR,  "span[id='promptResult']")
