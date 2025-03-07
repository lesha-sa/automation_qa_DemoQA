import allure
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators.WebTablePageLocators import WebTablePageLocators
from pages.base_page import BasePage


class WebTablePage(BasePage):
    """
    WebTablePage contains methods: 'add_new_person', 'check_new_added_person', 'search_some_person',
    'update_person_info', 'delete_person', 'check_deleted', 'select_up_to_some_rows', 'check_count_rows'
    """
    locators = WebTablePageLocators()

    @allure.step('Add new person')
    def add_new_person(self):
        """
        Fill in the person data and add it to the table using the generator
        :return: firstname, lastname, email, age, salary, department
        """
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            with allure.step('Click button add new person'):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
            with allure.step('Fill all fields'):
                self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
                self.element_is_visible(self.locators.SUBMIT).click()
                count -=1
                return [firstname, lastname,  str(age), email, str(salary), department]

    @allure.step('Check new added person')
    def check_new_added_person(self):
        """
        add all person in list for further comparison
        :return data
        """
        people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('Search some person')
    def search_some_person(self, key_word):
        """
        :param key_word: find some person
        :return:
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check search person')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person info')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person(self):
        """
        Delete person
        """
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check deleted')
    def check_deleted(self):
        """
        Check deleted person
        """
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Select up to some rows')
    def select_up_to_some_rows(self):
        """
        Select all the lines in turn
        :return: return the number of rows passed
        """
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Check count rows')
    def check_count_rows(self):
        """
        Go through all available lines
        :return: Length of the row list
        """
        list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)
