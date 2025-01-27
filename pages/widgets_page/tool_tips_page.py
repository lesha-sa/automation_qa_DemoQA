import time

from locators.widgets_page_locators.ToolTipsPageLocators import ToolTipsPageLocators
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    """
    ToolTipsPage contains methods: 'get_text_from_tool_tips', 'check_tool_tips',
    """
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        """
        The cursor moves to the center of the element
        Get the text from the hover, which appears when you hover over it
        Picking up the text after the hover
        :param hover_elem: element to be hovered over
        :param wait_elem: element to be waited for after hovering
        :return: text
        """
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        """
        Move the cursor over the element and wait for the element to appear.
        :return: tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
        """
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        time.sleep(1)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        time.sleep(1)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTARY_LINK)
        time.sleep(1)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION_LINK)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section