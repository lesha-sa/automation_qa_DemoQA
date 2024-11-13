import random

from locators.CheckBoxPageLocators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()
    """
    Click on the "+" button to open the full list Checkbox
    """
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
    """
    Randomly click on items from the checkbox list
    """
    def click_random_checkbox(self):
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
    """
    Create a list of clicked checkboxes. Format the list for further comparison with the output
    """
    def get_checked_checkboxes(self):
        checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()


    """
    Create a list of checkbox output. Format the list for further comparison with the clicked checkbox
    """
    def get_output_result(self):
        result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()