from faker.generator import random

from locators.interactions_page_locators.SortablePageLocators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    """
    SortablePage contains methods: 'get_sortable_items', 'change_list_order', 'change_grid_order'
    """

    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        """
        create an item list
        :param elements:
        :return: [item.text for item in item_list]
        """
        item_list = self.element_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        """
        click on the tab list
        assign all items to order_before
        select 2 random items
        item_what = item_list[0]
        item_where = item_list[1]
        swap item_what and item_where
        assign the new list of items in order_after
        :return: order_before, order_after
        """
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self. get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self. get_sortable_items(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        """
        click on the tab list
        assign all items to order_before
        select 2 random items
        item_what = item_list[0]
        item_where = item_list[1]
        swap item_what and item_where
        assign the new list of items in order_after
        :return: order_before, order_after
        """
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self. get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.element_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self. get_sortable_items(self.locators.GRID_ITEM)
        return order_before, order_after


