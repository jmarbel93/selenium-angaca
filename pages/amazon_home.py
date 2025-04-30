from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonHome(BasePage):
       
    MUSIC_LINK = (By.CSS_SELECTOR, '[data-csa-c-content-id="nav_cs_music"]')        

    def click_music(self):
        self.click(self.MUSIC_LINK)
