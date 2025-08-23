# checkout.py
import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.locators import CheckoutLocators
from .base_page import BasePage


class CartCheckout(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # --- Cart ---
    def shopping_cart(self):
        self.click_if_exists(CheckoutLocators.SHOPPINGCART)

    def proceed_to_checkout(self):
        self.click_if_exists(CheckoutLocators.PROCEEDTOCHECKOUT)

    def is_guest_checkout_flow(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(CheckoutLocators.EMAILID)
            )
            print("Guest checkout flow detected")
            return True
        except TimeoutException:
            print("Logged-in checkout flow detected")
            return False

    # --- Email ---
    def email_id(self, email_id):
        try:
            self.send_keys(CheckoutLocators.EMAILID, email_id)
            return True
        except Exception as e:
            print(f"Failed to fill email: {e}")
            return False

    # --- Checkout Fields ---
    def fname(self, value): self.fill_if_exists(CheckoutLocators.FNAME, value)
    def lname(self, value): self.fill_if_exists(CheckoutLocators.LNAME, value)
    def company(self, value): self.fill_if_exists(CheckoutLocators.COMPANY, value)
    def streetadd1(self, value): self.fill_if_exists(CheckoutLocators.STREETADD1, value)
    def streetadd2(self, value): self.fill_if_exists(CheckoutLocators.STREETADD2, value)
    def streetadd3(self, value): self.fill_if_exists(CheckoutLocators.STREETADD3, value)
    def city(self, value): self.fill_if_exists(CheckoutLocators.CITY, value)
    def state(self, value): self.fill_if_exists(CheckoutLocators.STATE, value)
    def zip(self, value): self.fill_if_exists(CheckoutLocators.ZIP, value)
    def phone(self, value): self.fill_if_exists(CheckoutLocators.PHONE, value)

    def country(self, country_name, timeout=10):
        try:
            dropdown = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(CheckoutLocators.COUNTRY)
            )
            dropdown.click()
            time.sleep(1)
            self.select_by_visible_text(CheckoutLocators.COUNTRY, country_name)
            return True
        except TimeoutException:
            print(f"Country dropdown not ready within {timeout}s")
            return False
        except Exception as e:
            print(f"Country selection failed: {e}")
            return False

    # --- Shipping & Payment ---
    def shipping_method0(self):
        return self.click_if_exists(CheckoutLocators.SHIPPING_METHOD)

    def shipping_method(self):
        return self.click_if_exists(CheckoutLocators.SHIPPING_METHOD)

    def click_next(self):
        clicked = self.click_if_exists(CheckoutLocators.NEXT0)
        print("Next button clicked" if clicked else "Next button not found")
        return clicked

    def nextbtn(self):
        return self.click_with_loader_wait(CheckoutLocators.NEXTBTN)

    def acknowledge(self):
        return self.click_if_exists(CheckoutLocators.ACKNOWLEDGE)

    def placeOrder0(self):
        return self.click_if_exists(CheckoutLocators.PLACEORDER0)

    def placeorder(self):
        return self.click_with_loader_wait(CheckoutLocators.PLACEORDER)
