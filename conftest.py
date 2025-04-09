import pytest
from selenium import webdriver 

@pytest.fixture(scope="function")
def driver(request):
    """"I have copied this fixture from a tutorial
    It will allow me to initialize the Webdriver based on CLI argument
    """
    
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    # This will provide the driver instance to the test
    yield driver  
    # and the close the driver after test text execution
    driver.quit()  

# This adds a command line option for selecting the browser
# by default it will be chrome
def pytest_addoption(parser):
    
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox, edge")
