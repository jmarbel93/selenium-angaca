from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AmazonSearchResults(BasePage):
    
    NAVBAR_LOGO = (By.ID, 'navbarMusicLogo')  
    BRAND_CHECKBOX = (By.XPATH, "//*[@id='brandsRefinements']//div[following-sibling::span[text()='{}'] ]//i")
    ORDERBY_DROPDOWN = (By.ID, "a-autoid-0-announce")
    ORDERBY_DROPDOWN_OPTION = (By.ID, "s-result-sort-select_{}")
    RESULT_LIST = (By.CLASS_NAME, "s-result-list")
    PRICES = (By.XPATH, "(//div[@data-cy='price-recipe']//span[@class='a-price']//span[@class='a-offscreen'])")

    
        
    def is_visible(self):
        return self.driver.find_elements(*self.NAVBAR_LOGO)
    
    def click_brand_checkbox(self, brand):
        locator = (
            self.BRAND_CHECKBOX[0],                  
            self.BRAND_CHECKBOX[1].format(brand)    
        )
        self.click(locator)
        
    
        
        
    def order_results_by(self,option):
        
        """
            Chooses orderby dropdown option:
            0 - Destacados
            1 - Precio: De menor a mayor
            2 - Precio: De mayor a menor
            3 - Promedio Opiniones de clientes
            4 - Lanzamientos recientes
            5 - Los mas vendidos
            
        """
        
        self.click(self.ORDERBY_DROPDOWN)
        
        locator = (
            self.ORDERBY_DROPDOWN_OPTION[0],                  
            self.ORDERBY_DROPDOWN_OPTION[1].format(option)    
        )
        self.click(locator)
        
    def get_prices(self, limit=None):
        return self.driver.find_elements(*self.PRICES)[:limit]
