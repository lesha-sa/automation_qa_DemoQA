import allure

from locators.alerts_frame_windows_page_locators.ModalDialogsPageLocators import ModalDialogsPageLocators
from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    """
    FramePage contains methods: 'check_model_dialogs'
    """
    locators = ModalDialogsPageLocators()

    @allure.step('Checl model dialogs')
    def check_model_dialogs(self):
        """
        Click on Small modal button, parse title and text from body, close
        Click on Large modal button, parse title and text from body, close
        :return: [title_small, len(body_small_text)], [title_large, len(body_large_text)]
        """

        self.element_is_visible(self.locators.SMALL_MODEL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODEL_TITLE).text
        body_small_text = self.element_is_visible(self.locators.SMALL_MODEL_BODY).text
        self.element_is_visible(self.locators.SMALL_MODEL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODEL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODEL_TITLE).text
        body_large_text = self.element_is_visible(self.locators.LARGE_MODEL_BODY).text
        self.element_is_visible(self.locators.LARGE_MODEL_CLOSE_BUTTON).click()
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]




