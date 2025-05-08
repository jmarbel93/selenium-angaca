from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonMusic(BasePage):
    
    # aqui los locators esos 
    NAVBAR_LOGO = (By.ID, 'navbarMusicLogo')  
    
    # aqui las acciones y las mierdas 
    
    def is_visible(self):
        return self.driver.find_elements(*self.NAVBAR_LOGO)
    
    
    def write_in_search_bar(text):
        self.enter_text()
        


    # def enter_text(self, locator, text):
    #         element = self.wait_for_element(locator)
    #         element.clear()
    #         element.send_keys(text)