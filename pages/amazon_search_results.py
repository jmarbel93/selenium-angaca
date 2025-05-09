from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonSearchResults(BasePage):
    
    NAVBAR_LOGO = (By.ID, 'navbarMusicLogo')  
    PUMA_CHECKBOX = (By.XPATH, "//li[.//span[contains(text(), 'PUMA')]]//i[contains(@class, 'a-icon-checkbox')]")
    ORDERBY_DROPDOWN = (By.ID, "a-autoid-0-announce")
    ORDERBY_DROPDOWN_ASCENDING_PRICE_OPTION = (By.ID, "s-result-sort-select_1")
    RESULT_LIST = (By.CLASS_NAME, "s-result-list")
    PRICES = (By.XPATH, "(//div[@data-component-type='s-search-result']//span[@class='a-price']//span[@class='a-offscreen'])[position() <= 10]")

    
        
    def is_visible(self):
        return self.driver.find_elements(*self.NAVBAR_LOGO)
    
    def click_PUMA_checkbox(self):
        self.click(self.PUMA_CHECKBOX)
        
    def click_orderby_dropdown(self):
        self.click(self.ORDERBY_DROPDOWN)
        
    def click_orderby_dropdown_ascending_price_option(self):
        self.click(self.ORDERBY_DROPDOWN_ASCENDING_PRICE_OPTION)
        
    def get_first_ten_prices(self):
            prices = self.driver.find_elements(*self.PRICES)
            return prices
