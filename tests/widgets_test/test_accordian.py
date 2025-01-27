from pages.widgets_page.accordian_page import AccordianPage
from read_configuration import read_configuration


class TestAccordingPage:

    def test_accordian(self, driver):
        url = read_configuration()
        accordian_page = AccordianPage(driver, f'{url}/accordian')
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and len(first_content) > 0, 'Incorrect title or missing text'
        assert second_title == 'Where does it come from?' and len(second_content) > 0, 'Incorrect title or missing text'
        assert third_title == 'Why do we use it?' and len(third_content) > 0, 'Incorrect title or missing text'