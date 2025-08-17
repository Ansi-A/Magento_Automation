import time
import traceback
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.locators import CheckoutLocators
from pages.base_page import BasePage


class Item_Selection(BasePage):
    def __init__(self, driver, timeout=15):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    # ---------- Helper Methods ----------
    def wait_for_loader(self):
        """Wait until the page loader disappears"""
        try:
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.loading-mask")))
        except Exception:
            pass  # Ignore if loader doesn't appear

    def safe_click(self, element):
        """Scroll into view and click safely using JS fallback"""
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    # ---------- Main Actions ----------
    def search_item(self, query):
        """Search for an item"""
        try:
            srch_box = self.wait.until(EC.element_to_be_clickable(CheckoutLocators.SEARCH))
            srch_box.click()
            srch_box.send_keys(query)
            srch_box.send_keys(Keys.ENTER)

            # Wait for results to load
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search.results")))
            return True
        except Exception:
            print("[ERROR] Search failed:\n", traceback.format_exc())
            self.driver.save_screenshot("search_failed.png")
            return False

    def select_item(self):
        """Click on the first item in search results"""
        try:
            self.wait_for_loader()
            product = self.wait.until(lambda d: d.find_element(*CheckoutLocators.ITEMSELECTION))
            self.safe_click(product)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-info-main")))
            return True
        except Exception:
            print("[ERROR] Item selection failed:\n", traceback.format_exc())
            self.driver.save_screenshot("item_selection_failed.png")
            return False

    def select_size(self):
        """Select item size"""
        try:
            self.wait_for_loader()
            size_btn = self.wait.until(EC.element_to_be_clickable(CheckoutLocators.ITEMSIZE))
            self.safe_click(size_btn)
            return True
        except Exception:
            print("[ERROR] Size selection failed:\n", traceback.format_exc())
            self.driver.save_screenshot("size_selection_failed.png")
            return False

    def select_color(self):
        """Select item color"""
        try:
            self.wait_for_loader()
            color_btn = self.wait.until(EC.element_to_be_clickable(CheckoutLocators.ITEMCOLOR))
            self.safe_click(color_btn)
            return True
        except Exception:
            print("[ERROR] Color selection failed:\n", traceback.format_exc())
            self.driver.save_screenshot("color_selection_failed.png")
            return False

    def set_quantity(self, quantity, max_retries=3):
        """Set item quantity with retries"""
        for attempt in range(max_retries):
            try:
                self.wait_for_loader()
                qty_input = self.wait.until(EC.element_to_be_clickable(CheckoutLocators.ITEMQTY))
                qty_input.clear()
                qty_input.send_keys(str(quantity))
                if qty_input.get_attribute("value") == str(quantity):
                    return True
            except Exception:
                print(f"[WARNING] Quantity attempt {attempt + 1} failed:\n", traceback.format_exc())
                self.driver.refresh()
                time.sleep(1)
        self.driver.save_screenshot("qty_failed.png")
        return False

    def checkout(self):
        """Click 'Add to Cart' and verify success"""
        try:
            self.wait_for_loader()
            checkout_btn = self.wait.until(EC.element_to_be_clickable(CheckoutLocators.CHECKOUT))
            self.safe_click(checkout_btn)
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message-success")))
            return True
        except Exception:
            print("[ERROR] Checkout failed:\n", traceback.format_exc())
            return False
