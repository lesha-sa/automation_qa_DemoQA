from selenium.webdriver.common.by import By


class TabsPageLocators:
    """
    Locators for the page https://demoqa.com/tabs
    """
    TABS_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')