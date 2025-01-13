from selenium.webdriver.common.by import By



class TextBoxPageLocators:
    """
    Locators for the page https://demoqa.com/text-box
    """
    #form_page fields
    FULL_NAME = (By.CSS_SELECTOR, 'input[placeholder="Full Name"]')
    EMAIL = (By.XPATH, '//*[@placeholder="name@example.com"]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id = "currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//*[@id = "permanentAddress"]')
    SUBMIT = (By.XPATH, '//*[@id = "submit"]')

    # created form_page
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')