from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonMusic(BasePage):
    
    MUSIC_LOGO = (By.ID, 'navbarMusicLogox')    
    
    def are_we_in_amazon_music(self):
        return self.is_element_visible(self.MUSIC_LOGO)
    