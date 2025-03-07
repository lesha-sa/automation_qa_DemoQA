import allure

from pages.alerts_frame_windows_page.nested_frame_page import NestedFramePage
from read_configuration import read_configuration

@allure.suite('Alerts frame windows')
@allure.feature('Nested frame page')
class TestNestedFramePage:

    @allure.title('Nested frame')
    def test_nested_frame(self, driver):
        url = read_configuration()
        nested_frame_page = NestedFramePage(driver, f'{url}/nestedframes')
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frame()
        assert parent_text == 'Parent frame', 'Nested frame does not exist'
        assert child_text == 'Child Iframe', 'Nested frame does not exist'