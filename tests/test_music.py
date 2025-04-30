import time
from pages.amazon_home import AmazonHome
from pages.amazon_music import AmazonMusic
from config import get_base_url
import time


def test_music(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_music = AmazonMusic(driver)    
    

    driver.get(get_base_url())
    
    
    amazon_home.click_music()

    
    assert amazon_music.is_visible()
