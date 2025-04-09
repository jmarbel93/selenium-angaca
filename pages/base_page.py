from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    # driver will be passed to the constructor of the page classes that inherit from this class 
    #  when we create a instance of them in the test
    def __init__(self, driver):
        self.driver = driver
    
    # this method waits for a element to be present and then returns it or raises a timeout exception 
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    

    def click(self, locator):
        self.wait_for_element(locator).click()
        

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        
    
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
        