import os

from selenium.webdriver import Keys

from generator.generator import generated_file, generated_person, generated_subject
from locators.form_page_locators.FormPageLocators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    """
    FormPage contains methods: 'fill_form_fields', 'form_result'
    """

    locators = FormPageLocators()

    def fill_form_fields(self):
        """
        Fill in the form with data
        :return: filled form
        """
        person = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys(generated_subject())
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.go_to_element(self.element_is_present(self.locators.FILE_INPUT))
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        """
        Create a list with the data received from the form for further comparison
        :return: data list
        """
        result_list = self.element_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data