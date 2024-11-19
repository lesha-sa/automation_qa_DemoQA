from pages.elements_page.radio_button_page import RadioButtonPage
from read_configuration import read_configuration


class TestRadioButton:

    def test_radio_button(self, driver):
        url = read_configuration()
        radio_button_page = RadioButtonPage(driver, f'{url}/radio-button')
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', '"Yes" have not been selected'
        assert output_impressive == 'Impressive', '"Impressive" have not been selected'
        #assert output_no == 'No', '"No" have not been selected'
