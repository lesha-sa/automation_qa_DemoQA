from faker.generator import random
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators.AutoCompletePageLocators import AutoCompletePageLocators
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    """
    AutoCompletePage contains methods: 'fill_input_multi', 'remove_value_from_multi',
    'check_color_in_multi', 'fill_input_single', 'check_color_in_single'
    """
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        """
        Add a random number of colors and add 1 each to the color variable
        add color to input, press Enter
        :return: color
        """
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2,5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        """
        Take the number of colors before removal and after removal
        Remove only 1 color
        :return: count_value_before, count_value_after
        """
        count_value_before = len(self.element_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.element_are_visible(self.locators.MULTI_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.element_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        """
        Create a list of colors for comparison
        :return: colors
        """
        color_list = self.element_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        """
        Send a random color to input and hit enter.
        :return: color
        """
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        """
        Color check
        :return: color.text
        """
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text