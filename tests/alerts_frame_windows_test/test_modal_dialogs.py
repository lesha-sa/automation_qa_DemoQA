import allure

from pages.alerts_frame_windows_page.nested_frame_page import NestedFramePage
from read_configuration import read_configuration
from pages.alerts_frame_windows_page.modal_dialogs_page import ModalDialogsPage


@allure.suite('Alerts frame windows')
@allure.feature('Nested Frame Page')
class TestNestedFramePage:

    @allure.title('Modal dialogs')
    def test_modal_dialogs(self, driver):
        url = read_configuration()
        modal_dialogs_page = ModalDialogsPage(driver, f'{url}/modal-dialogs')
        modal_dialogs_page.open()
        small, large = modal_dialogs_page.check_model_dialogs()
        assert small[1] < large[1], 'text from large dialog is less than text from small dialog'
        assert small[0] == 'Small Modal', 'The header is not "Small modal"'
        assert large[0] == 'Large Modal', 'The header is not "Large modal"'