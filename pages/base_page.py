from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import get_timeout


class BasePage:

    
    def __init__(self, driver):
        self.driver = driver
        
    
    def wait_for_element(self, locator: tuple, timeout=None):
        if timeout is None:
            timeout = get_timeout()
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
    )
    

    def click(self, locator):
        self.wait_for_element(locator).click()
        

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
