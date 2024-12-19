import requests

from locators.LinksPageLocators import LinksPageLocators
from pages.base_page import BasePage


class LinksPage(BasePage):
    """
    LinksPage contains methods: 'check_new_tab_simple_link', 'check_broken_list'
    """
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        """
        assign the simple_link attribute to link_href
        if the status code is 200
        then open simple_link, switch to a new window and save the result in the URL
        otherwise return link_href and status code
        :return: link_href, url for comparison
        """
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code


    def check_broken_list(self, url):
        """
        send get request to url and if status code 200 click on link
otherwise return status code
        :param url:
        :return: request.status_code
        """
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code
