import allure

from pages.elements_page.check_box_page import CheckBoxPage
from read_configuration import read_configuration

@allure.suite('Elements')
@allure.feature('CheckBox')
class TestCheckBox:

    @allure.title('Check Box')
    def test_check_box(self, driver):
        url = read_configuration()
        check_box_page = CheckBoxPage(driver, f'{url}/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_checkbox = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_checkbox)
        assert input_checkbox == output_checkbox, 'checkboxes have not been selected'