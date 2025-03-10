import allure

from pages.base_page import BasePage
from locators.elements_page_locators.RadioButtonPageLocators import RadioButtonPageLocators


class RadioButtonPage(BasePage):
    """
    RadioButtonPage contains methods: 'click_on_the_radio_button', 'get_output_result'
    """
    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio button')
    def click_on_the_radio_button(self, choice):
        """
        Create a dictionary with 3 keys: Yes, Impressive, No
        :param choice: Click on each key
        """
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                    'no':self.locators.NO_RADIOBUTTON,}
        self.element_is_visible(choices[choice]).click()

    @allure.step('Get output result')
    def get_output_result(self):
        """
        :return: output result text clicked item
        """
        return self.element_is_present(self.locators.OUTPUT_RESULT).text