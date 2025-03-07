import base64
import os

import allure
from faker.generator import random

from generator.generator import generated_file
from locators.elements_page_locators.UploadAndDownloadPageLocators import UploadAndDownloadPageLocators
from pages.base_page import BasePage


class UploadAndDownloadPage(BasePage):
    """
    LinksPage contains methods: 'upload_file', 'download_file'
    """

    locators = UploadAndDownloadPageLocators()

    @allure.step('Upload file')
    def upload_file(self):
        """
        Generate a new file
        Send the file path to input
        Then delete file
        Assign the file path to the text variable
        :return: formatted results file_name, text
        """
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self):
        """
        Assign the link attribute to the link
        Link_b decoding link
        Download the file
        :return:
        """
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\proj\automation_qa_DemoQA\filetest{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file