from selenium.webdriver.common.by import By


class AutoCompletePageLocators:
    """
    Locators for the page https://demoqa.com/auto-complete
    """
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class ="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_REMOVE = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"] svg path')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class ="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id = "autoCompleteSingleInput"]')
