import time
from pages.amazon_home import AmazonHome
from pages.amazon_music import AmazonMusic
from pages.amazon_search_results import AmazonSearchResults
from config import get_base_url


def test_music(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_music = AmazonMusic(driver)    
    

    driver.get(get_base_url())
    
    
    amazon_home.click_music()

    
    assert amazon_music.is_visible()
    
    

def test_PUMA(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_search_results = AmazonSearchResults(driver)    


    driver.get(get_base_url())
    
    
    amazon_home.enter_text_search_bar("zapatillas")
    
    
    amazon_home.click_search_submit()
    
    amazon_search_results.click_PUMA_checkbox()
    
    amazon_search_results.click_orderby_dropdown()
    
    amazon_search_results.click_orderby_dropdown_ascending_price_option()
    
    
    first_ten_prices = amazon_search_results.get_first_ten_prices()
    
    
    current_biggest_price = 0
    
    for i, price in enumerate(first_ten_prices):
        raw = price.get_attribute('textContent')
        numeric = float(raw.replace("€", "").replace(",", "."))
        
        print(f"{i+1}: {numeric}")
        assert numeric >= current_biggest_price
        current_biggest_price = numeric
