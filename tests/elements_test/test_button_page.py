import allure

from pages.elements_page.buttons_page import ButtonsPage
from read_configuration import read_configuration

@allure.suite('Elements')
@allure.feature('Buttons Page')
class TestButtonsPage:

    @allure.title('Different click on the buttons')
    def test_different_click_on_the_buttons(self, driver):
        url = read_configuration()
        button_page = ButtonsPage(driver, f'{url}/buttons')
        button_page.open()
        double = button_page.click_on_different_button('double')
        right = button_page.click_on_different_button('right')
        click = button_page.click_on_different_button('click')
        assert double == "You have done a double click", "The double click button was not pressed"
        assert right == "You have done a right click", "The right click button was not pressed"
        assert click == "You have done a dynamic click", "The dynamic click button was not pressed"