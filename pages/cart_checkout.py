# checkout.py
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
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

    def is_guest_checkout_flow(self, timeout=3):
        """
        Detects if the current checkout flow is for a guest (requires email)
        or a logged-in user (uses saved address).
        Returns True if guest flow (email field visible), False if user flow.
        """
        try:
            # Quick check if email field is present
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(CheckoutLocators.EMAILID)
            )
            print("🔍 Detected: Guest Checkout Flow (email field present)")
            return True
        except TimeoutException:
            print("🔍 Detected: Logged-in User Checkout Flow (no email field)")
            return False
    # ----------------- EMAIL (now also skip if missing) -----------------
    def email_id(self, email_id):
        """Use the robust send_keys method from base.py"""
        try:
            self.send_keys(CheckoutLocators.EMAILID, email_id)
            print(f"✅ Email filled: {email_id}")
            return True
        except Exception as e:
            print(f"❌ Failed to fill email: {e}")
            return False

    # ----------------- CHECKOUT FIELDS (all safe: exist => fill, else skip) -----------------

    def fname(self, value): self.fill_if_exists(CheckoutLocators.FNAME, value)
    def lname(self, value): self.fill_if_exists(CheckoutLocators.LNAME, value)
    def company(self, value): self.fill_if_exists(CheckoutLocators.COMPANY, value)
    def streetadd1(self, value): self.fill_if_exists(CheckoutLocators.STREETADD1, value)
    def streetadd2(self, value): self.fill_if_exists(CheckoutLocators.STREETADD2, value)
    def streetadd3(self, value): self.fill_if_exists(CheckoutLocators.STREETADD3, value)
    def city(self, value): self.fill_if_exists(CheckoutLocators.CITY, value)
    def state(self, value): self.fill_if_exists(CheckoutLocators.STATE, value)
    def zip(self, value): self.fill_if_exists(CheckoutLocators.ZIP, value)

    def country(self, country_name, timeout=10):
        """
        Robust country selection that waits for options to load via AJAX.
        """
        try:
            # 1. Wait for country dropdown to be clickable
            country_dropdown = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(CheckoutLocators.COUNTRY)
            )

            # 2. Click to open dropdown (triggers AJAX loading if needed)
            country_dropdown.click()
            time.sleep(1)  # Brief pause for options to load

            # 3. Select using the robust base method
            self.select_by_visible_text(CheckoutLocators.COUNTRY, country_name)
            print(f"✅ Country selected: {country_name}")
            return True

        except TimeoutException:
            print(f"[INFO] Country dropdown not ready within {timeout}s. Skipping.")
            return False
        except Exception as e:
            print(f"[INFO] Country selection failed: {e}")
            return False
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
        # REPLACED click_if_exists with click_with_loader_wait for this critical action
        return self.click_with_loader_wait(CheckoutLocators.NEXTBTN)

    def acknowledge(self):
        return self.click_if_exists(CheckoutLocators.ACKNOWLEDGE)

    def placeOrder0(self):
        return self.click_if_exists(CheckoutLocators.PLACEORDER0)

    def placeorder(self):
        # REPLACED click_if_exists with click_with_loader_wait for this critical action
        return self.click_with_loader_wait(CheckoutLocators.PLACEORDER)