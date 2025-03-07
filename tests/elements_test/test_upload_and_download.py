import allure

from pages.elements_page.upload_and_download_page import UploadAndDownloadPage
from read_configuration import read_configuration

@allure.suite('Elements')
@allure.feature('Upload and download')
class TestUploadAndDownload:

    @allure.title('Check upload file')
    def test_upload_file(self, driver):
        url = read_configuration()
        upload_page = UploadAndDownloadPage(driver, f'{url}/upload-download')
        upload_page.open()
        file_name, result = upload_page.upload_file()
        assert file_name == result, "the file has not benn uploaded"

    @allure.title('Check download file')
    def test_download_file(self, driver):
        url = read_configuration()
        download_page = UploadAndDownloadPage(driver, f'{url}/upload-download')
        download_page.open()
        check = download_page.download_file()
        assert check is True, "the file has not benn downloaded"
