from pages.elements_page.text_box_page import TextBoxPage
from read_configuration import read_configuration



class TestTextBox:
    def test_text_box(self, driver):
        url = read_configuration()
        text_box_page = TextBoxPage(driver, f'{url}/text-box')
        text_box_page.open()
        text_box_page.fill_all_field()
        full_name, email, current_address, permanent_address = text_box_page.check_filled_form()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
        assert full_name == output_name, 'the full name does not match'
        assert email == output_email, 'the email does not match'
        assert current_address == output_cur_address, 'the current address does not match'
        assert permanent_address == output_per_address, 'the permanent address does not match'