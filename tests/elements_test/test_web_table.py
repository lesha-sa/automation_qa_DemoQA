from itertools import count

from faker.generator import random

from pages.elements_page.web_table_page import WebTablePage
from read_configuration import read_configuration


class TestWebTable:

    def test_web_table_add_person(self, driver):
        """
        add new person to table
        """
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        print(new_person)
        print(table_result)
        assert new_person in table_result


    def test_web_table_search_person(self, driver):
        """
        search person in table
        """
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0,5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, 'the person was not found in the table'


    def test_web_table_update_person_info(self, driver):
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, "the person card has not been changed"

    def test_web_table_delete_person(self, driver):
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found"

    def test_web_table_change_count_row(self, driver):
        url = read_configuration()
        web_table_page = WebTablePage(driver, f'{url}/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50,
                         100], "The number of rows in table has not been changed or has changed incorrectly"