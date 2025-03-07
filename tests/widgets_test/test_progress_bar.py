import allure

from pages.widgets_page.progress_bar_page import ProgressBarPage
from read_configuration import read_configuration

@allure.suite('Widgets')
@allure.feature('Progress bar page')
class TestProgressBarPage:

    @allure.title('Progress bar')
    def test_progress_bar(self, driver):
        url = read_configuration()
        progress_bar_page = ProgressBarPage(driver, f'{url}/progress-bar')
        progress_bar_page.open()
        before, after = progress_bar_page.change_progress_bar_value()
        assert before != after, 'the progress bar value has not been change'
