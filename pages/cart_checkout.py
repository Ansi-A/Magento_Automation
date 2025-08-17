# checkout.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.locators import CheckoutLocators
from .base_page import BasePage

class CartCheckout(BasePage):
    """Handles all cart and checkout operations on Magento website."""

    def __init__(self, driver):
        super().__init__(driver)

    # ----------------- CART -----------------
    def shopping_cart(self):
        self.click_if_exists(CheckoutLocators.SHOPPINGCART)

    def proceed_to_checkout(self):
        self.click_if_exists(CheckoutLocators.PROCEEDTOCHECKOUT)

    # ----------------- EMAIL (now also skip if missing) -----------------
    def email_id(self, email_id):
        email_locator = (By.ID, "customer-email")
        try:
            field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(email_locator)
            )
            try:
                field.clear()
            except Exception:
                pass
            field.send_keys(email_id)
            print(f"✅ Email filled: {email_id}")
            return True
        except Exception:
            print("⚠️ Email field not found/visible. Skipping.")
            return False

    # ----------------- CHECKOUT FIELDS (all safe: exist => fill, else skip) -----------------

    def fname(self, value): self.fill_if_exists(CheckoutLocators.FNAME, value)
    def lname(self, value): self.fill_if_exists(CheckoutLocators.LNAME, value)
    def company(self, value): self.fill_if_exists(CheckoutLocators.COMPANY, value)
    def streetadd1(self, value): self.fill_if_exists(CheckoutLocators.STREETADD1, value)
    def streetadd2(self, value): self.fill_if_exists(CheckoutLocators.STREETADD2, value)
    def streetadd3(self, value): self.fill_if_exists(CheckoutLocators.STREETADD3, value)
    def city(self, value): self.fill_if_exists(CheckoutLocators.CITY, value)
    def state(self, value): self.select_if_exists(CheckoutLocators.STATE, value)
    def zip(self, value): self.fill_if_exists(CheckoutLocators.ZIP, value)
    def country(self, value): self.select_if_exists(CheckoutLocators.COUNTRY, value)
    def phone(self, value): self.fill_if_exists(CheckoutLocators.PHONE, value)
    # ----------------- SHIPPING & PAYMENT (all safe clicks) -----------------
    def shipping_method0(self):
        return self.click_if_exists(CheckoutLocators.SHIPPING_METHOD)

    def shipping_method(self):
        return self.click_if_exists(CheckoutLocators.SHIPPING_METHOD)

    def click_next(self):
        """Click 'Next' if present; else skip. Returns True/False."""
        # (fixed the earlier bug: don't .click() twice)
        clicked = self.click_if_exists(CheckoutLocators.NEXT0)
        print("Clicked 'Next' button" if clicked else "'Next' button not present - skipping")
        return clicked

    def nextbtn(self):
        return self.click_if_exists(CheckoutLocators.NEXTBTN)

    def acknowledge(self):
        return self.click_if_exists(CheckoutLocators.ACKNOWLEDGE)

    def placeOrder0(self):
        return self.click_if_exists(CheckoutLocators.PLACEORDER0)

    def placeorder(self):
        return self.click_if_exists(CheckoutLocators.PLACEORDER)
