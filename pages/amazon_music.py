from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonMusic(BasePage):
    
    NAVBAR_LOGO = (By.ID, 'navbarMusicLogo')  
    
    def is_visible(self):
        return self.driver.find_elements(*self.NAVBAR_LOGO)
