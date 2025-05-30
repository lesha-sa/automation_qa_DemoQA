import allure

from pages.widgets_page.slider_page import SliderPage
from read_configuration import read_configuration

@allure.suite('Widgets')
@allure.feature('Slider page')
class TestSliderPage:

    @allure.title('Slider')
    def test_slider(self, driver):
        url = read_configuration()
        slider_page = SliderPage(driver, f'{url}/slider')
        slider_page.open()
        before, after = slider_page.change_slider_value()
        assert before != after, 'the slider value has not been change'


