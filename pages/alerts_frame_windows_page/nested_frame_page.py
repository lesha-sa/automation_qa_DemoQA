from locators.alerts_frame_windows_page_locators.NestedFramePageLocators import NestedFramePageLocators
from pages.base_page import BasePage


class NestedFramePage(BasePage):
    """
    NestedFramePage contains methods: 'check_frame'
    """
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        """
        Switch to the parent frame, parse the text
        Switch to the child frame, parse text
        :return: parent_text, child_text
        """
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.select_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.select_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text
