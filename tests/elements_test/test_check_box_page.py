from pages.elements_page.check_box_page import CheckBoxPage
from conftest import driver


class TestCheckBox:
    def test_check_box(self, driver):
        base_url = 'https://demoqa.com'
        check_box_page = CheckBoxPage(driver, f"{base_url}/checkbox")
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_checkbox = check_box_page.get_output_result()
        print(input_checkbox)
        print(output_checkbox)
        assert input_checkbox == output_checkbox, 'checkboxes have not been selected'