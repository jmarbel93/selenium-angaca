from pages.amazon_home import AmazonHome
from pages.amazon_music import AmazonMusic
from pages.amazon_search_results import AmazonSearchResults
from config import get_base_url


def test_user_can_navigate_to_the_amazon_music_page(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_music = AmazonMusic(driver)    
    

    driver.get(get_base_url())
    
    
    amazon_home.click_music()

    
    assert amazon_music.is_visible(), "Amazon Music page is not visible at this point"
    
    

def test_user_is_able_to_search_and_filter_for_products(driver):
    
    
    amazon_home = AmazonHome(driver)
    amazon_search_results = AmazonSearchResults(driver)    


    driver.get(get_base_url())
    
    
    amazon_home.enter_text_search_bar("zapatillas")
    
    
    amazon_home.click_search_submit()
    
    
    amazon_search_results.click_brand_checkbox("PUMA")
    
    
    amazon_search_results.order_results_by(1)
    
    
    
    search_result_prices = amazon_search_results.get_prices(10)
    
    
    current_biggest_price = 0
    
    
    for i, price in enumerate(search_result_prices):
        
        raw = price.get_attribute('textContent')
        numeric = float(raw.replace("€", "").replace(",", "."))
        
        print(f"{i+1}: {numeric}")
        assert numeric >= current_biggest_price, f"Assert error: '{current_biggest_price}' is higher than '{numeric}'"
        current_biggest_price = numeric
