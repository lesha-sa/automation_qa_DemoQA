import allure
from faker.generator import random

from locators.interactions_page_locators.SelectablePageLocators import SelectablePageLocators
from pages.base_page import BasePage


class SelectablePage(BasePage):
    """
    SelectablePage contains methods: 'click_selectable_item', 'select_list_item', 'select_grid_item'
    """

    locators = SelectablePageLocators()

    @allure.step('Click selectable item')
    def click_selectable_item(self, elements):
        """
        Assign all items in item_list
        Click on 1 random item
        """
        item_list = self.element_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('Select list item')
    def select_list_item(self):
        """
        Click on Tab List
        Select 1 random item from the List
        assign to the clicked element in active_element
        :return: active_element.text
        """
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @allure.step('Select grid item')
    def select_grid_item(self):
        """
        Click on Tab Grid
        Select 1 random item from the List
        assign to the clicked element in active_element
        :return: active_element.text
        """
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text