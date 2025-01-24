import random

from locators.widgets_page_locators.SliderPageLocators import SliderPageLocators
from pages.base_page import BasePage


class SliderPage(BasePage):
    """
    SliderPage contains methods: 'change_slider_value'
    """

    locators = SliderPageLocators()

    def change_slider_value(self):
        """
        Pass data slider to value_before
        Move the slider to a random value
        Pass the received data slider to value_after
        :return: value_before, value_after
        """

        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after