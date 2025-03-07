import allure

from pages.interactions_page.sortable_page import SortablePage
from read_configuration import read_configuration

@allure.suite('Interactions')
@allure.feature('Sortable page')
class TestSortablePage:

    @allure.title('Sortable')
    def test_sortable(self, driver):
        url = read_configuration()
        sortable_page = SortablePage(driver, f'{url}/sortable')
        sortable_page.open()
        list_before, list_after = sortable_page.change_list_order()
        grid_before, grid_after = sortable_page.change_grid_order()
        assert list_after != list_before, 'the order of the list has not been changed'
        assert grid_before != grid_after, 'the order of the grid has not been changed'