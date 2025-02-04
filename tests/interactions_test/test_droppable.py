from pages.interactions_page.droppable_page import DroppablePage
from read_configuration import read_configuration


class TestDroppablePage:

    def test_simple_droppable(self, driver):
        url = read_configuration()
        droppable_page = DroppablePage(driver, f'{url}/droppable')
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', 'the elements has not been dropped'

    def test_accept_droppable(self, driver):
        url = read_configuration()
        droppable_page = DroppablePage(driver, f'{url}/droppable')
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()
        assert not_accept == 'Drop here', 'the dropped element has been accepted'
        assert accept == 'Dropped!', 'the dropped element has not been accepted'

    def test_prevent_droppable(self, driver):
        url = read_configuration()
        droppable_page = DroppablePage(driver, f'{url}/droppable')
        droppable_page.open()
        not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
        assert not_greedy == 'Dropped!', 'the elements texts has not been changed'
        assert not_greedy_inner == 'Dropped!', 'the elements texts has not been changed'
        assert greedy == 'Outer droppable', 'the elements texts has not been changed'
        assert greedy_inner == 'Dropped!', 'the elements texts has not been changed'

    def test_revert_draggable_droppable(self, driver):
        url = read_configuration()
        droppable_page = DroppablePage(driver, f'{url}/droppable')
        droppable_page.open()
        will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
        not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
        assert will_after_move != will_after_revert, 'the elements has not reverted'
        assert not_will_after_move == not_will_after_revert, 'the elements has  reverted'