from locators.alerts_frame_windows_page_locators.FramePageLocators import FramePageLocators
from pages.base_page import BasePage


class FramePage(BasePage):
    """
    FramePage contains methods: 'check_frame'
    """
    locators = FramePageLocators()

    def check_frame(self, frame_num):
        """
        Find the frame, its width and height, switch to the frame, take the text from it
        Switch to the main window
        :param frame_num: frame number for check
        :return: text, width, height
        """
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.select_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.select_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]