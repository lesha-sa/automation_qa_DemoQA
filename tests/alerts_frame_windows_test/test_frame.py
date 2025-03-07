import allure

from pages.alerts_frame_windows_page.frame_page import FramePage
from read_configuration import read_configuration

@allure.suite('Alerts frame windows')
@allure.feature('Frame Page')
class TestFramePage:

    @allure.title('Frame')
    def test_frame(self, driver):
        url = read_configuration()
        frame_page = FramePage(driver, f'{url}/frames')
        frame_page.open()
        result_frame1 = frame_page.check_frame('frame1')
        result_frame2 = frame_page.check_frame('frame2')
        assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
        assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'
