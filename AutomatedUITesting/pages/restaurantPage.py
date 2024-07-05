from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basePage import BasePage
from utils.data_helpers import read_menu_data

class RestaurantPage(BasePage):

    def view_menu(self):
        self.click_element((By.XPATH, "//div[@id='mat-tab-label-0-0']"))

    def check_menu_categories_visibility(self):
        menu_category_xpath = (By.XPATH, "//div[@class='header-wrapper']/div[@class='header ng-star-inserted']/span")
        menu_categories = self.find_elements(menu_category_xpath)
        assert len(menu_categories) > 0, "Menü kategorileri görünmüyor."
        return [category.text for category in menu_categories]

    def search_menu(self, search_term):
        self.driver.execute_script("window.scrollTo(0, 400)")
        self.send_keys_to_element((By.XPATH, "(//input[@type='text'])[2]"), search_term)

        WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.CLASS_NAME, "menu-item-detail"))
        )

    def verify_search_result(self, search_term):
        results = self.find_elements((By.CLASS_NAME, "menu-item-detail"))
        found = any(search_term in result.text for result in results)
        assert found, f"{search_term} bulunamadı!"
        return found

    def add_product_to_cart(self):
        self.click_element((By.CSS_SELECTOR, ".menu-item:nth-child(1) .add-button"))
        self.click_element((By.XPATH, "//span[contains(.,'Sepete Ekle')]"))

    def go_to_cart(self):
        self.click_element((By.ID, "homepage-cart-button"))


    def verify_product_in_cart(self, product_name):
        self.go_to_cart()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart-item"))
        )
        cart_items = self.find_elements((By.CLASS_NAME, "cart-item"))
        found = any(product_name in item.text for item in cart_items)
        assert found, f"{product_name} sepette bulunamadı!"
        return found



    def get_menu_product_names(self):

        product_divs = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "menu-item-detail")))

        product_names = []

        for i, product_div in enumerate(product_divs):
            if i >= 5:
                break
            
            span_elements = product_div.find_elements(By.CLASS_NAME, 'subtitle-2')
            if span_elements:
                product_name = span_elements[0].text.strip()
                product_names.append(product_name)

        return product_names

    def get_menu_product_prices(self):
        product_divs = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "menu-item-detail")))

        product_prices = []

        for i, product_div in enumerate(product_divs):
            if i >= 5:
                break
            
            try:
                price_element = product_div.find_element(By.XPATH, './/div[@class="price-wrapper"]/h3')
                product_price = price_element.text.strip()
                product_prices.append(product_price)
            except Exception as e:
                print(f"Fiyat bulunamadı: {str(e)}")

        return product_prices


    def verify_menu_data_with_excel(self, sheet_name):
        menu_data = read_menu_data(sheet_name)
        web_product_names = self.get_menu_product_names()
        web_product_prices = self.get_menu_product_prices()

        for product_name, product_price in menu_data:
            assert product_name in web_product_names, f"{product_name} web sayfasında bulunamadı!"
            assert product_price in web_product_prices, f"{product_name} ürününün fiyatı web sayfasında {product_price} olarak bulunamadı!"
