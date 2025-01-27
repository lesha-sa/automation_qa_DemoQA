from read_configuration import read_configuration


class TestSortablePage:

    def test_sortable(self, driver):
        url = read_configuration()
        menu_page = SortablePage(driver, f'{url}/sortable')
        menu_page.open()