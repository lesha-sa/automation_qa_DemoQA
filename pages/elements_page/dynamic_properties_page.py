import time

from selenium.common import TimeoutException

from locators.elements_page_locators.DynamicPropertiesPageLocators import DynamicPropertiesPageLocators
from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    """
    DynamicPropertiesPage contains methods: 'check_enable_button', 'check_changed_of_color', 'check_appear_button'
    """
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        """
        Wait 5 seconds and try to press
        :return: the result
        """
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True


    def check_changed_of_color(self):
        """
        Pass the color before the change and the color after 5 seconds to the variable
        :return: both variables
        """
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return  color_button_before, color_button_after

    def check_appear_button(self):
        """
        Wait 5 seconds and try to press
        :return: the result
        """
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutException:
            return False
        return True