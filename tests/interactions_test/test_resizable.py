from pages.interactions_page.resizable_page import ResizablePage
from read_configuration import read_configuration


class TestResizablePage:

    def test_resizable_page(self, driver):
        url = read_configuration()
        resizable_page = ResizablePage(driver, f'{url}/resizable')
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        max_resize, min_resize = resizable_page.change_size_resizable()
        assert ('500px', '300px') == max_box, 'maximum size not equal to "500px", "300px"'
        assert ('150px', '150px') == min_box, 'minimum size not equal to "150px", "150px"'
        assert min_resize != max_resize, 'resizable has not been changed'