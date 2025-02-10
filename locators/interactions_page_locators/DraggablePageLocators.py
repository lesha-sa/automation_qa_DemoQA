from selenium.webdriver.common.by import By


class DraggablePageLocators:
    """
    Locators for the page https://demoqa.com/dragabble
    """
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')
    #Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')