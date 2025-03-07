import allure
from selenium.common import TimeoutException

from locators.widgets_page_locators.AccordianPageLocators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    """
    AccordianPage contains methods: 'check_accordian'
    """

    locators = AccordianPageLocators()

    @allure.step('Check accordian')
    def check_accordian(self, accordian_num):
        """
        Create a dictionary for element reference and fill it with widget data
        Search for a title and click on it
        Try to parse the content text
        If exeption, click on the title and parse content text
        :param accordian_num: section name
        :return: [section_title.text, section_content]
        """
        accordian = {'first': {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third': {'title': self.locators.SECTION_THIRD,
                                'content': self.locators.SECTION_CONTENT_THIRD}
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text

        return [section_title.text, section_content]