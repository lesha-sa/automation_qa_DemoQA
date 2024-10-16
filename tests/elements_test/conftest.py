import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

'''@pytest.fixture()
def setup_and_teardown(request, session_logger):
    """
    Setup browser and make first steps on the home page
    """
    browser = request.param.get("browser")
    browser_headless_mode = utils.str_to_bool(request.param.get("browser_headless_mode")) посмотреть, как работает

    if browser == "chrome":
        options = ChromeOptions()
        if browser_headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if browser_headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        if browser_headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    else:
       print(
            "Config file has no name for the browser instance. Check the configuration. "
            "Acceptable browsers are: 'chrome', 'firefox', 'edge'")
    raise ValueError(f"Unsupported browser: {browser}")

    url = request.param.get("url")
    driver.get(url)
    request.cls.driver = driver  # Attaching driver to the class under tests
    yield driver
    driver.quit() '''


