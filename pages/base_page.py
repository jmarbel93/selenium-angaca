from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import get_timeout


class BasePage:

    
    def __init__(self, driver):
        self.driver = driver
        
    
    def wait_for_element(self, locator: tuple, timeout=None):
        """
        Waits for an element to be present on the page.

        Parameters:
            locator (tuple): A locator tuple (By.<METHOD>, "value") used to find the element.
            timeout (int, optional): How long to wait in seconds. Defaults to value from config.

        Returns:
            WebElement: The found element once it becomes present in the DOM.
        """
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
