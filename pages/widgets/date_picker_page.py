from selenium.webdriver.support.select import Select

from generator.generator import generated_date
from locators.widgets_page_locators.DatePickerPageLocators import DatePickerPageLocators
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    """
    AccordianPage contains methods: 'select_date', 'select_date_and_time', 'set_date_by_text',
     'set_date_item_from_list'
    """


    locators = DatePickerPageLocators()


    def select_date(self):
        """
        Click on the date input and select a value and click on it
        Select month, year, day
        :return: value_date_before, value_date_after
        """
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


    def select_date_and_time(self):
        """
        Click on the date input and select a value and click on it
        Select month, year, day and time
        :return: value_date_before, value_date_after
        """
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST,date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST,'2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST,date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST,date.time)
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after


    def set_date_by_text(self, element, value):
        """
        Selecting by visible text
        """
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        """
        Select a date from the data list
        """
        item_list = self.element_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break