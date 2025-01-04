from pages.elements_page.dynamic_properties_page import DynamicPropertiesPage
from read_configuration import read_configuration


class TestDynamicPropertiesPage:

    def test_check_enable_button(self, driver):
        url = read_configuration()
        dynamic_properties_page = DynamicPropertiesPage(driver, f'{url}/dynamic-properties')
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, 'button did not enable after 5 second'

    def test_color_change_button(self, driver):
        url = read_configuration()
        dynamic_properties_page = DynamicPropertiesPage(driver, f'{url}/dynamic-properties')
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_after != color_before, 'colors have not been changed'

    def test_check_appear_button(self, driver):
        url = read_configuration()
        dynamic_properties_page = DynamicPropertiesPage(driver, f'{url}/dynamic-properties')
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_button()
        assert appear is True, 'button did not appear after 5 second'