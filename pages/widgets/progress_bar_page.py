import random
import time

from locators.widgets_page_locators.ProgressBarPageLocators import ProgressBarPageLocators
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    """
    ProgressBarPage contains methods: 'change_progress_bar_value'
    """

    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        """
        Pass progress bar data to value_before
        Click on progress bar
        After a random interval, click on progress bar again.
        Pass the received data progress bar to value_after
        :return: value_before, value_after
        """
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2,5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_after,value_before