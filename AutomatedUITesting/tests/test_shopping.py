from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.basePage import BasePage
from pages.mainPage import MainPage
from pages.restaurantPage import RestaurantPage
from pages.cartPage import CartPage
from utils.data_helpers import read_menu_data

class TestSiparis:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito") 
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.migros.com.tr/yemek")
        self.driver.maximize_window()

    def run_test(self):
        base_page = BasePage(self.driver)
        main_page = MainPage(self.driver)

        # Anasayfa erişimi doğruluğu
        assert main_page.is_page_loaded(), "Anasayfa yüklenemedi."

        main_page.add_address()
        main_page.close_cookies()
        base_page.window_scrollTo()
        time.sleep(2)
        main_page.select_restaurant()
        main_page.continue_without_membership()
        time.sleep(2)
        main_page.select_restaurant()



        restaurant_page = RestaurantPage(self.driver)

        # Menü kategorileri Görünürlüğü ve Listeleme
        restaurant_page.view_menu()
        restaurant_page.check_menu_categories_visibility()

        # Menü fiyat doğruluğu
        restaurant_page.verify_menu_data_with_excel("Sayfa1")

        # Restoran menüsünde ürün arama ve doğruluğu
        restaurant_page.search_menu("Salata")
        assert restaurant_page.verify_search_result("Salata"), "Arama sonucu doğrulaması başarısız oldu."

        # Ürünün sepete eklenmesi ve kontrolü
        restaurant_page.add_product_to_cart()
        assert restaurant_page.verify_product_in_cart("Mevsim Salata"), "Ürün sepette bulunamadı."


        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        # Sepette ürün miktarını arttırma
        cart_page.increase_product_quantity()
        # Sepette ürün miktarını azaltma
        cart_page.decrease_product_quantity()
        # Sepetten ürün çıkarma
        cart_page.remove_product_from_cart()

if __name__ == "__main__":
    test = TestSiparis()
    test.run_test()
