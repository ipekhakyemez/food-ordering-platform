from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class CartPage(BasePage):

    def go_to_cart(self):
        self.click_element((By.ID, "homepage-cart-button"))

    def increase_product_quantity(self):
        self.click_element((By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .product-actions > #product-actions-product-increase--mevsim-salata-p-19986 .svg-inline--fa"))

    def decrease_product_quantity(self):
        self.click_element((By.CSS_SELECTOR, ".ng-star-inserted:nth-child(2) > .product-actions > #product-actions-product-decrease--mevsim-salata-p-19986 .svg-inline--fa"))

    def remove_product_from_cart(self):
        self.click_element((By.ID, "cart-page-item-remove"))
