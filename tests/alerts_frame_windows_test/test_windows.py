from pages.alerts_frame_windows_page.windows_page import BrowserWindowsPage
from read_configuration import read_configuration


class TestBrowserWindows:

    def test_new_tab(self, driver):
        url = read_configuration()
        browser_new_tab_page = BrowserWindowsPage(driver, f'{url}/browser-windows')
        browser_new_tab_page.open()
        text_result = browser_new_tab_page.check_opened_new_tab()
        assert text_result == 'This is a sample page', "A new tab has not opened or an incorrect tab has opened"


    def test_new_window(self, driver):
        url = read_configuration()
        browser_window_page = BrowserWindowsPage(driver, f'{url}/browser-windows')
        browser_window_page.open()
        text_result = browser_window_page.check_opened_new_window()
        assert text_result == 'This is a sample page',"A new window has not opened or an incorrect window has opened"