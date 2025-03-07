import allure

from pages.elements_page.text_box_page import TextBoxPage
from read_configuration import read_configuration
from logger_config.logger import get_logger

logger = get_logger()

@allure.suite(''"Elements")
@allure.feature('TextBox')
class TestTextBox:

    @allure.title('Check TextBox')
    def test_text_box(self, driver):
        url = read_configuration()
        logger.debug(f"read configuration {url}/text-box")
        text_box_page = TextBoxPage(driver, f'{url}/text-box')
        logger.debug("update home page to text-box-page")
        text_box_page.open()
        logger.debug("open text-box-page")
        text_box_page.fill_all_field()
        logger.debug("fill all fields")
        """
        Comparison of text output and input
        """
        full_name, email, current_address, permanent_address = text_box_page.check_filled_form()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()

        try:
            full_name == output_name
            logger.info('the full name match')
        except:
            logger.error('the full name does not match')
        try:
            email == output_email
            logger.info('the email match')
        except:
            logger.error('the email does not match')
        try:
            current_address == output_cur_address
            logger.info('the current address match')
        except:
            logger.error('the current address does not match')
        try:
            permanent_address == output_per_address
            logger.info('the permanent address match')
        except:
            logger.error('the permanent address does not match')