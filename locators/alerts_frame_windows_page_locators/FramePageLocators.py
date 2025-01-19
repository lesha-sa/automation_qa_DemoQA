from selenium.webdriver.common.by import By


class FramePageLocators:
    """
    Locators for the page https://demoqa.com/frames
    """
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")