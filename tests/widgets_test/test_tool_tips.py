from pages.widgets.tool_tips_page import ToolTipsPage
from read_configuration import read_configuration


class TestToolTipsPage:

    def test_tool_tips_page(self, driver):
        url = read_configuration()
        tool_tips_page = ToolTipsPage(driver, f'{url}/tool-tips')
        tool_tips_page.open()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'
