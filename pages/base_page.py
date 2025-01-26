from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from tests.alerts_frame_windows_test.conftest import driver


class BasePage:
    """
    Contains methods for finding elements on a page
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=2):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=2):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_down(self, locator, timeout=2):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def select_new_window(self):
        tab = self.driver.window_handles
        select_new_tab = self.driver.switch_to.window(tab[1])
        return select_new_tab

    def select_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except TimeoutException:
            print("no alert")

    def select_frame(self, frame_name):
        frame = self.driver.switch_to.frame(frame_name)
        return frame

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
