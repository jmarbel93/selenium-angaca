from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonHome(BasePage):
       
    MUSIC_LINK = (By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_music"]')
    
    SEARCH_TEXT_INPUT = (By.ID, 'twotabsearchtextbox')       

    def click_music(self):
        self.click(self.MUSIC_LINK)

    def click_music(self):
        self.click(self.MUSIC_LINK)
