import re

import allure
from faker.generator import random

from locators.interactions_page_locators.DraggablePageLocators import DraggablePageLocators
from pages.base_page import BasePage


class DraggablePage(BasePage):
    """
    DraggablePage contains methods: 'get_before_and_after_position', 'simple_drag_box',
    'get_top_position', 'get_left_position', 'axis_restricted'
    """
    locators = DraggablePageLocators

    @allure.step('Get before and after position')
    def get_before_and_after_position(self, drag_element):
        """
        Moves the drag box and writes the “style” attribute data to the before_position variable
        Moves the drag box and writes the “style” attribute data to the after_position variable
        :param drag_element
        :return: drag_element: before_position, after_position
        """
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Simple drag box')
    def simple_drag_box(self):
        """
        Select drag box and pass data to before_position, after_position
        :return: before_position, after_position
        """
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    @allure.step('Get top position')
    def get_top_position(self, positions):
        """
        Format the data for future use
        """
        return re.findall(r'\d[0-9] | \d', positions.split(';')[2])

    @allure.step('Get left position')
    def get_left_position(self, positions):
        """
        Format the data for future use
        """
        return re.findall(r'\d[0-9] | \d', positions.split(';')[1])

    @allure.step('Axis restricted')
    def axis_restricted(self,type_axis):
        """
        Create a dictionary for selecting a box by the keys:
        'axis_x'(Only X) or 'axis_y'(Only Y)
        Click on the tab 'Axis Restricted'
        Select axis_type
        Get the position of the axis
        Pass data to variables before and after position change
        :param type_axis:
        :return: [top_position_before, top_position_after], [left_position_before, left_position_after]
        """
        axis = {
            'axis_x':
                {'axis': self.locators.ONLY_X},
            'axis_y':
                {'axis': self.locators.ONLY_Y}
        }
        self.element_is_visible(self.locators.AXIS_TAB).click()
        axis_type = self.element_is_visible(axis[type_axis]['axis'])
        position = self.get_before_and_after_position(axis_type)
        top_position_before = self.get_top_position(position[0])
        top_position_after = self.get_top_position(position[1])
        left_position_before = self.get_left_position(position[0])
        left_position_after = self.get_left_position(position[1])
        return [top_position_before, top_position_after], [left_position_before, left_position_after]
