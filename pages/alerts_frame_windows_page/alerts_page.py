import random
import time

from locators.alerts_frame_windows_page_locators.AlertsPageLocators import AlertsPageLocators
from pages.base_page import BasePage


class AlertsPage(BasePage):
    """
    AlertsPage contains methods: 'check_see_alert', 'check_alert_appear_5_sec',
    'check_confirm_alert', 'check_confirm_alert'
    """

    locators = AlertsPageLocators()

    def check_see_alert(self):
        """
        Click on the button and switch to alerts
        :return: alert
        """
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert = self.select_alert()
        return alert

    def check_alert_appear_5_sec(self):
        """
        Click on the button, wait 5 seconds and switch to alerts
        :return: alert
        """
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(7)
        alert = self.select_alert()
        return alert

    def check_confirm_alert(self):
        """
        Click on the button, switch to alerts and confirm
        :return: text result
        """
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_promt_alert(self):
        """
        Click on the button, switch to alerts, send text and random number in the range 0 - 999б and confirm
        :return: generated text, text result
        """
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT).text
        return text, text_result