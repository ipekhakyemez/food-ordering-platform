from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class MainPage(BasePage):

    def is_page_loaded(self):
        try:
            self.find_element((By.ID, "header-yemek-tab"))
            return True
        except:
            return False


    def add_address(self):
        self.send_keys_to_element((By.XPATH, "//*[@id='mat-input-0']"), "Akşemsettin, Korkutata Sk. 50/A, 34762 Fatih/İstanbul, Türkiye")
        self.click_element((By.XPATH, "//*[@id='mat-mdc-dialog-0']/div/div/fe-delivery-options-modal/mat-dialog-content/div/fe-delivery-location-map-modal/div/fe-location-selection-map/form/div/li"))
        self.click_element((By.XPATH, "//*[@id='add-location-btn']/span[2]"))
        self.click_element((By.XPATH, "//*[@id='location-verify-btn']/span[2]"))

    def close_cookies(self):
        self.click_element((By.XPATH, "//*[@id='reject-all']"))

    def select_restaurant(self):
        self.click_element((By.XPATH, "//img[@alt='Adile Sultan Ev Yemekleri, Fatih (Silivrikapı Mah.)']"))

    def continue_without_membership(self):
        self.click_element((By.XPATH, "//span[contains(.,'Üye Olmadan Devam Et')]"))
