import time

from pages.form_page.form_page import FormPage
from read_configuration import read_configuration


class TestFormPage:
    def test_form(self, driver):
        url = read_configuration()
        form_page = FormPage(driver, f'{url}/automation-practice-form')
        form_page.open()
        person_info = form_page.fill_form_fields()
        result = form_page.form_result()
        assert [person_info.firstname + " " + person_info.lastname, person_info.email] == [result[0], result[1]], \
            "the form has not been filled"
