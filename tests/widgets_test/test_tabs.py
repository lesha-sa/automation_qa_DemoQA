from pages.widgets.tabs_page import TabsPage
from read_configuration import read_configuration


class TestTabsPage:

    def test_tabs(self, driver):
        url = read_configuration()
        tabs_page = TabsPage(driver, f'{url}/tabs')
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content= tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        more_button, more_content = tabs_page.check_tabs('more')
        assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
        assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
        assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'
        assert more_button == 'More' and more_content != 0, 'the tab "more" was not pressed or the text is missing'