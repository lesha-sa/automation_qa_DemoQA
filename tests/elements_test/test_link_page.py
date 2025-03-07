import allure

from pages.elements_page.links_page import LinksPage
from read_configuration import read_configuration


@allure.suite('Elements')
@allure.feature('Link page')
class TestLinkPage:

    @allure.title('Check link')
    def test_check_link(self, driver):
        url = read_configuration()
        links_page = LinksPage(driver, f'{url}/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, 'the link is broken or url is incorrect'

    @allure.title('Check broken link')
    def test_broken_link(self, driver):
        url = read_configuration()
        links_page = LinksPage(driver, f'{url}/links')
        links_page.open()
        response_code = links_page.check_broken_list('https://demoqa.com/bad-request')
        assert response_code == 400, 'the link works or the status code is son 400 '
