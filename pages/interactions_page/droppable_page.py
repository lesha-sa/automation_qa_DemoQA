import time

import allure

from locators.interactions_page_locators.DroppablePageLocators import DroppablePageLocators
from pages.base_page import BasePage


class DroppablePage(BasePage):
    """
    DroppablePage contains methods: 'drop_simple', 'drop_accept',
    'drop_prevent_propogation', 'drop_revert_draggable'
    """
    locators = DroppablePageLocators()

    @allure.step('Drop simple')
    def drop_simple(self):
        """
        Click on the tab 'Simple'
        assign box 'Drag me' to the drag_div
        assign box 'Drop here' to the drop_div
        move drag_div to drop_div
        :return: drop_div.text
        """
        self.element_is_present(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('Drop accept')
    def drop_accept(self):
        """
        Click on the tab 'Accept'
        assign box 'Acceptable' to the acceptable_div
        assign box 'Not Acceptable' to the not_acceptable_div
        assign box 'Drop here' to the drop_div
        move not_acceptable_div to drop_div
        assign drop_div.text to the drop_text_not_accept
        move acceptable_div to drop_div
        assign drop_div.text to the drop_text_accept
        :return: drop_text_not_accept, drop_text_accept
        """
        self.element_is_present(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    @allure.step('Drop prevent propogation')
    def drop_prevent_propogation(self):
        """
        Click on the tab 'Prevent Propogation'
        assign box 'Drag me' to the drag_div
        assign box 'Inner droppable (not greedy)' to the not_greedy_inner_box
        assign box 'Inner droppable (greedy)' to the greedy_inner_box
        move drag_div to not_greedy_inner_box
        assign box 'Inner droppable (not greedy).text' to the text_not_greedy_box
        assign box 'Outer droppable.text' to the text_not_greedy_inner_box
         move drag_div to greedy_inner_box
        assign box 'Inner droppable (greedy).text' to the text_greedy_box
        assign box 'Outer droppable.text' to the text_greedy_inner_box
        :return: text_not_greedy_box, text_not_greedy_inner_box,text_greedy_box, text_greedy_inner_box
        """
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box,text_greedy_box, text_greedy_inner_box

    @allure.step('Drop revert draggable')
    def drop_revert_draggable(self, type_drag):
        """
        Create a dictionary for selecting a box by the keys:
        'will'(Will Revert) or 'not_will'(Not Revert)
        Click on the tab 'Prevent Propogation'
        assign box 'Will Revert' or 'Not Revert' to the revert
        assign box 'Drop Here' to the drop_div
        move revert to drop_div
        assign the 'style' attribute to position_after_move
        time.sleep(1)
        assign the 'style' attribute to position_after_revert
        :param type_drag:
        :return: position_after_move, position_after_revert
        """
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT, },
            'not_will':
                {'revert': self.locators.NOT_REVERT},
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert