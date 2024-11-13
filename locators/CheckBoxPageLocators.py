from selenium.webdriver.common.by import By

"""
Locators for the page https://demoqa.com/checkbox
"""

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']") #
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ('.//ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")