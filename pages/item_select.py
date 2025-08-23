import time
from selenium.webdriver import Keys
from utils.locators import CheckoutLocators
from pages.base_page import BasePage


class Item_Selection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # ---------- Main Actions ----------
    def search_item(self, query):
        """Search for an item using base.py methods"""
        try:
            # Use elementtobeclickable from base.py
            srch_box = self.elementtobeclickable(CheckoutLocators.SEARCH)
            srch_box.click()
            srch_box.send_keys(query)
            srch_box.send_keys(Keys.ENTER)

            # Wait for results using base.py method - FIXED
            self.presenceofelementlocated(CheckoutLocators.SEARCH)
            return True
        except Exception:
            print("[ERROR] Search failed")
            self.driver.save_screenshot("search_failed.png")
            return False

    def select_item(self):
        """Click on the first item in search results"""
        try:
            self.wait_for_loader_to_disappear()
            product = self.elementtobeclickable(CheckoutLocators.ITEMSELECTION)
            product.click()
            # Wait for product page using base.py method - FIXED
            self.presenceofelementlocated(CheckoutLocators.ITEMSELECTION)
            return True
        except Exception:
            print("[ERROR] Item selection failed")
            self.driver.save_screenshot("item_selection_failed.png")
            return False

    def select_size(self):
        """Select item size"""
        try:
            self.wait_for_loader_to_disappear()
            size_btn = self.elementtobeclickable(CheckoutLocators.ITEMSIZE)
            size_btn.click()
            return True
        except Exception:
            print("[ERROR] Size selection failed")
            self.driver.save_screenshot("size_selection_failed.png")
            return False

    def select_color(self):
        """Select item color"""
        try:
            self.wait_for_loader_to_disappear()
            color_btn = self.elementtobeclickable(CheckoutLocators.ITEMCOLOR)
            color_btn.click()
            return True
        except Exception:
            print("[ERROR] Color selection failed")
            self.driver.save_screenshot("color_selection_failed.png")
            return False

    def set_quantity(self, quantity, max_retries=3):
        """Set item quantity with retries"""
        for attempt in range(max_retries):
            try:
                self.wait_for_loader_to_disappear()
                qty_input = self.elementtobeclickable(CheckoutLocators.ITEMQTY)
                qty_input.clear()
                qty_input.send_keys(str(quantity))
                if qty_input.get_attribute("value") == str(quantity):
                    return True
            except Exception:
                print(f"[WARNING] Quantity attempt {attempt + 1} failed")
                self.driver.refresh()
                time.sleep(1)
        self.driver.save_screenshot("qty_failed.png")
        return False

    def checkout(self):
        """Click 'Add to Cart' and verify success"""
        try:
            self.wait_for_loader_to_disappear()
            checkout_btn = self.elementtobeclickable(CheckoutLocators.CHECKOUT)
            checkout_btn.click()
            # Wait for success message using base.py method - FIXED
            self.visibilityofelement(CheckoutLocators.CHECKOUT)
            return True
        except Exception:
            print("[ERROR] Checkout failed")
            return False