import time

import allure

from pages.widgets_page.autocomplete_page import AutoCompletePage
from read_configuration import read_configuration

@allure.suite('Widgets')
@allure.feature('Autocomplete page')
class TestAutoCompletePage:

    @allure.title('Fill multi autocomplete')
    def test_fill_multi_autocomplete(self, driver):
        url = read_configuration()
        autocomplete_page = AutoCompletePage(driver, f'{url}/auto-complete')
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result, 'the added colors are missing in the input'

    @allure.title('Remove value from multi')
    def test_remove_value_from_multi(self, driver):
        url = read_configuration()
        autocomplete_page = AutoCompletePage(driver, f'{url}/auto-complete')
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, color_value_after = autocomplete_page.remove_value_from_multi()
        assert color_value_after != count_value_before, 'value was not deleted'

    @allure.title('Single autocomplete')
    def test_single_autocomplete(self,driver):
        url = read_configuration()
        autocomplete_page = AutoCompletePage(driver, f'{url}/auto-complete')
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result, 'the added color are missing in the input'
