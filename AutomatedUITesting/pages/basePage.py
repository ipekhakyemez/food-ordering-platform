from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, explicit_wait_timeout=30):
        self.driver = driver
        self.explicit_wait_timeout = explicit_wait_timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.explicit_wait_timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.explicit_wait_timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys_to_element(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    def window_scrollTo(self):
        self.driver.execute_script("window.scrollTo(0, 400)")
