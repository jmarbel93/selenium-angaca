from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    
    def __init__(self, driver):
        self.driver = driver
        
    
    def wait_for_element(self, locator:tuple, timeout=10):
        """
        Wait for an element to be present in the DOM.
        :param locator: The locator of the element to wait for.
        :param timeout: The maximum time to wait for the element (in seconds).
        :return: The WebElement if found."""

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
    )
    

    def click(self, locator):
        self.wait_for_element(locator).click()
        

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
