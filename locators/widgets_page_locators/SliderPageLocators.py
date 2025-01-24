from selenium.webdriver.common.by import By


class SliderPageLocators:
    """
    Locators for the page https://demoqa.com/slider
    """

    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[class="form-control"]')