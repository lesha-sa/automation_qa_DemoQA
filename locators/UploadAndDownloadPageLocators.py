from selenium.webdriver.common.by import By

class UploadAndDownloadPageLocators:
    """
    Locators for the page https://demoqa.com/upload-download
    """
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath')
    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')