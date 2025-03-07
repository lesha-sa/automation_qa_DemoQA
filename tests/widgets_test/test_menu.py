import allure

from pages.widgets_page.menu_page import MenuPage
from read_configuration import read_configuration

@allure.suite('Widgets')
@allure.feature('Menu page')
class TestMenuPage:

    @allure.title('Menu items')
    def test_menu_items(self, driver):
        url = read_configuration()
        menu_page = MenuPage(driver, f'{url}/menu')
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'menu items do not exist or have not been selected'