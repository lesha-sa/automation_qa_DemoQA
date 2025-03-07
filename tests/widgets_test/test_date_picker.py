import allure
from attr import dataclass

from pages.widgets_page.date_picker_page import DatePickerPage
from read_configuration import read_configuration

@allure.suite('Widgets')
@allure.feature('Date picker page')
class TestDatePickerPage:

    @allure.title('Change date')
    def test_change_date(self, driver):
        url = read_configuration()
        date_picker_page = DatePickerPage(driver, f'{url}/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_after != value_date_before, 'the date has not been changed'

    @allure.title('Change date and time')
    def test_change_date_and_time(self, driver):
        url = read_configuration()
        date_picker_page = DatePickerPage(driver, f'{url}/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_after != value_date_before, 'the date and time have not been changed'