import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config import get_browser, is_headless

@pytest.fixture(scope="function")
def driver(request):
    cli_browser = request.config.getoption("--browser")
    browser = (cli_browser or get_browser()).strip().lower()
    headless = is_headless()  

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")  # "--headless" for older versions
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default=None,  
        help="Browser to use for tests: chrome, firefox, edge"
    )
