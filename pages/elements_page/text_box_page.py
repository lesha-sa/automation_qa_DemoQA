from generator.generator import generated_person
from locators.elements_page_locators.TextBoxPageLocators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """
    TextBoxPage contains methods: 'fill_all_field', 'check_filled_form'
    """
    locators = TextBoxPageLocators()

    def fill_all_field(self):
        """
        Using data generated by the generator to fill in fields
        for further comparison
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.go_down(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address


    def check_filled_form(self):
        """
        Take the output data for further comparison of the input and output text
        """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address