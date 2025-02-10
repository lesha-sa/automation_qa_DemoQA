from pages.interactions_page.draggable_page import DraggablePage
from read_configuration import read_configuration


class TestDraggablePage:

    def test_simple_draggable(self, driver):
        url = read_configuration()
        draggable_page = DraggablePage(driver, f'{url}/dragabble')
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()
        assert before != after, 'the position of the box has not been changed'

    def test_axis_restricted_draggable(self, driver):
        url = read_configuration()
        draggable_page = DraggablePage(driver, f'{url}/dragabble')
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted('axis_x')
        top_y, left_y = draggable_page.axis_restricted('axis_y')
        assert top_x[0][0] == top_x[1][0] and int(
            top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
        assert left_x[0][0] != left_x[1][0] and int(
            left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
        assert top_y[0][0] != top_y[1][0] and int(
            top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
        assert left_y[0][0] == left_y[1][0] and int(
            left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"
