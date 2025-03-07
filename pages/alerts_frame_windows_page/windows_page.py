import allure

from locators.alerts_frame_windows_page_locators.WindowsPageLocators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    """
    BrowserWindowsPage contains methods: 'check_opened_new_tab', 'check_opened_new_window'
    """

    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab')
    def check_opened_new_tab(self):
        """
        Click on the button, go to the new tab that opens, and take the text from the new tab
        :return: text_title
        """
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.select_new_window()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    @allure.step('Check opened new window')
    def check_opened_new_window(self):
        """
        Click on the button, go to the new window that opens, and take the text from the new window
        :return: text_title
        """
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.select_new_window()
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

