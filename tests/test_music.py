import time
from pages.amazon_home import AmazonHome
from pages.amazon_music import AmazonMusic
from selenium.webdriver.common.by import By

def test_music(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_music = AmazonMusic(driver)    
    

    driver.get("https://www.amazon.es")
    
    
    amazon_home.click_music()

    
    assert amazon_music.is_visible()
