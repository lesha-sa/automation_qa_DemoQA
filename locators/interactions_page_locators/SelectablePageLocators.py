from selenium.webdriver.common.by import By


class SelectablePageLocators:
    """
    Locators for the page https://demoqa.com/selectable
    """
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (
        By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item active list-group-item-action"]')