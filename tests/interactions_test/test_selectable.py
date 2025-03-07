import allure

from pages.interactions_page.selectable_page import SelectablePage
from read_configuration import read_configuration

@allure.suite('Interactions')
@allure.feature('Selectable page')
class TestSelectablePage:

    @allure.title('Selectable page')
    def test_selectable_page(self, driver):
        url = read_configuration()
        selectable_page = SelectablePage(driver, f'{url}/selectable')
        selectable_page.open()
        item_list = selectable_page.select_list_item()
        item_grid = selectable_page.select_grid_item()
        assert len(item_list) > 0, 'no elements were selected'
        assert len(item_grid) > 0, 'no elements were selected'