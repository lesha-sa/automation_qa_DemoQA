from pages.elements_page import CheckBoxPage
from conftest import driver


class TestCheckBox:
    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_check_box()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_checkbox = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_checkbox, 'checkboxes have not been selected'