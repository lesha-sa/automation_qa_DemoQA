import random

import allure

from locators.elements_page_locators.CheckBoxPageLocators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    """
    CheckBoxPage contains methods: 'open_full_list', 'click_random_checkbox',
    'get_checked_checkboxes', 'get_output_result'
    """
    locators = CheckBoxPageLocators()

    @allure.step("Open full list")
    def open_full_list(self):
        """
        Click on the "+" button to open the full list Checkbox
        """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step("Check random checkbox")
    def click_random_checkbox(self):
        """
        21 Times randomly click on items from the checkbox list
        """
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step("Get checked checkbox")
    def get_checked_checkboxes(self):
        """
        Create a list of clicked checkboxes. Format the list for further comparison with the output
        """
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()


    @allure.step("Get output result")
    def get_output_result(self):
        """
        Create a list of checkbox output. Format the list for further comparison with the clicked checkbox
        """
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
