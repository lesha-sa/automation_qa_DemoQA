from selenium.webdriver.common.by import By

class WebTablePageLocators:
   """
   Locators for the page https://demoqa.com/webtables
   """
   #add person form_page
   ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
   FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
   LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
   EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
   AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
   SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
   DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
   SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

   #tables
   FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
   SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
   DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
   ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
   NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
   COUNT_ROW_LIST = (By.CSS_SELECTOR,' select[aria-label="rows per page"]')

   #update
   UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')