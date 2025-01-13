from locators.elements_page_locators.ButtonsPageLocators import ButtonsPageLocators
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    """
    ButtonsPage contains methods: 'click_on_different_button', 'check_clicked_on_the_button'
    """
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        """
        Perform the required type of click on the button
        :param type_click:
        :return: The text of the result that appears after clicking for further comparison
        """
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)


    def check_clicked_on_the_button(self, element):
        """
        :param element:
        :return: confirmation text after correct type of button click
        """
        return self.element_is_present(element).text