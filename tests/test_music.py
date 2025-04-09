
import time
from pages.amazon_home import AmazonHome
from pages.amazon_music import AmazonMusic



def test_music(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_music = AmazonMusic(driver)    
    

    driver.get("https://www.amazon.es")

    time.sleep(10)

    
    amazon_home.click_music()

    time.sleep(10)
    
    assert amazon_music.are_we_in_amazon_music()
