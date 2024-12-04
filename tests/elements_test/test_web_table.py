from faker.generator import random

from pages.elements_page.web_table_page import WebTablePage
from read_configuration import read_configuration


class TestWebTable:

    def test_web_table_add_person(self, driver):
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        print(new_person)
        print(table_result)
        assert new_person in table_result


    def test_web_table_search_person(self, driver):
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0,5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, 'the person was not found in the table'