from selenium.webdriver.common.by import By


class ToolTipsPageLocators:
    """
    Locators for the page https://demoqa.com/tool-tips
    """
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTARY_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')
    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')