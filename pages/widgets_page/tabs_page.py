from locators.widgets_page_locators.TabsPageLocators import TabsPageLocators
from pages.base_page import BasePage


class TabsPage(BasePage):
    """
    TabsPage contains methods: 'test_tabs'
    """

    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        """
        Fill the dictionary with the name of the tabs and their contents
        click on a title
        fetch the tab text
        :param name_tab:
        :return: button.text, len(content)
        """
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(content)
