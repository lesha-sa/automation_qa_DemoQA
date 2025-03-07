import allure
from faker.generator import random

from locators.interactions_page_locators.ResizablePageLocators import ResizablePageLocators
from pages.base_page import BasePage


class ResizablePage(BasePage):
    """
    ResizablePage contains methods: 'get_px_from_width_height', 'get_max_min_size',
    'change_size_resizable_box', 'change_size_resizable'
    """

    locators = ResizablePageLocators()

    @allure.step('Get px from width height')
    def get_px_from_width_height(self, value_of_size):
        """
        Get the width and height
        :param value_of_size:
        :return: width, height
        """
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return  width, height

    @allure.step('Get max min size')
    def get_max_min_size(self, element):
        """
        Get the maximum and minimum size of the element
         :param element
        :return: size_value
        """
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('Change size resizable box')
    def change_size_resizable_box(self):
        """
        Dragging an element with a specified offset
        Assign sizes in max_size
        Dragging an element with a specified offset
        Assign sizes in min_size
        :return: max_size, min_size
        """
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change size resizable')
    def change_size_resizable(self):
        """
        Dragging an element with a specified offset
        Assign sizes in max_size
        Dragging an element with a specified offset
        Assign sizes in min_size
        :return: max_size, min_size
        """
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300),random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size



