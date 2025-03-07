import allure

from locators.widgets_page_locators.MenuPageLocators import MenuPageLocators
from pages.base_page import BasePage


class MenuPage(BasePage):
    """
    MenuPage contains methods: 'check_menu'
    """

    locators = MenuPageLocators()

    @allure.step('Check menu')
    def check_menu(self):
        """
        Save all items in the list
        Then hover each element of the list and add text to data
        :return: data
        """
        menu_item_list = self.element_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data