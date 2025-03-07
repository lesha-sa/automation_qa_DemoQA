import allure
from selenium.webdriver.common.devtools.v85.page import print_to_pdf

from pages.alerts_frame_windows_page.alerts_page import AlertsPage
from read_configuration import read_configuration


@allure.suite('Alerts frame windows')
@allure.feature('Alerts Page')
class TestAlertsPage:

    @allure.title('See alert')
    def test_see_alert(self, driver):
        url = read_configuration()
        alert_page = AlertsPage(driver, f'{url}/alerts')
        alert_page.open()
        alert_text = alert_page.check_see_alert()
        assert alert_text == 'You clicked a button', 'Alert did not show up'

    @allure.title('Alert appear 5 sec')
    def test_alert_appear_5_sec(self, driver):
        url = read_configuration()
        alert_page = AlertsPage(driver, f'{url}/alerts')
        alert_page.open()
        alert_text = alert_page.check_alert_appear_5_sec()
        assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

    @allure.title('Confirm alert')
    def test_confirm_alert(self, driver):
        url = read_configuration()
        alert_page = AlertsPage(driver, f'{url}/alerts')
        alert_page.open()
        alert_text = alert_page.check_confirm_alert()
        assert alert_text == 'You selected Ok', 'Alert did not show up'

    @allure.title('Promt alert')
    def test_promt_alert(self, driver):
        url = read_configuration()
        alert_page = AlertsPage(driver, f'{url}/alerts')
        alert_page.open()
        text, alert_text = alert_page.check_promt_alert()
        assert alert_text == f'You entered {text}', 'The text in the alert is different'