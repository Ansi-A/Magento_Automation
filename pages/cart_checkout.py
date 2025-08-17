import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from utils.locators import CheckoutPage, SelectItem


class CartCheckout(BasePage):
    """Handles all cart and checkout operations on Magento website."""

    def __init__(self, driver):
        super().__init__(driver)


    # ----------------- CART COUNTER -----------------
    '''    def wait_for_counter_update(self, timeout=10):
        """Wait for cart counter to update after adding item."""
        try:
            # Wait for spinner to disappear (if any)
            self.invisibilityofelement((By.CSS_SELECTOR, "img[alt='Loading...']"), timeout=timeout)
        except:
            pass

        def counter_updated(driver):
            element = driver.find_element(*CheckoutPage.nocounter)
            return element.text.isdigit() and int(element.text) > 0

        try:
            WebDriverWait(self.driver, timeout).until(counter_updated)
            return True
        except:
            return False
'''
    # ----------------- CHECKOUT FORM -----------------
    def shopping_cart(self):
        self.elementtobeclickable(CheckoutPage.shoppingcart).click()

    def proceed_to_checkout(self):


        self.elementtobeclickable(CheckoutPage.proceedtocheckout).click()

    def email_id(self, email_id):
        email_locator = (By.ID, "customer-email")
        wait = WebDriverWait(self.driver, 20)

        try:
            email_field = wait.until(
                EC.visibility_of_element_located(email_locator)
            )
            email_field.clear()
            email_field.send_keys(email_id)
            print("✅ Email filled:", email_id)
        except TimeoutException:
            # Debug info
            print("⚠️ Email field not found on checkout page")
            print("Current URL:", self.driver.current_url)
            self.driver.save_screenshot("email_debug.png")
            print(self.driver.page_source[:1000])
            raise  # stop test here so you know email wasn’t filled

    def shipping_method(self, shipping_method_value):
        try:
            self.elementtobeclickable(
                (CheckoutPage.shippingmethod)
            ).click()
            print(f"[INFO] Selected shipping method: {shipping_method_value}")
        except:
            print(f"[INFO] Shipping method '{shipping_method_value}' not found. Skipping.")

    def fname(self, fname):
        field = self.elementtobeclickable(CheckoutPage.fname)
        field.clear()
        field.send_keys(fname)

    def lname(self, lname):
        field = self.elementtobeclickable(CheckoutPage.lname)
        field.clear()
        field.send_keys(lname)

    def company(self, company):
        field = self.elementtobeclickable(CheckoutPage.company)
        field.clear()
        field.send_keys(company)

    def streetadd1(self, streetadd1):
        field = self.elementtobeclickable(CheckoutPage.streetadd1)
        field.clear()
        field.send_keys(streetadd1)

    def streetadd2(self, streetadd2):
        field = self.elementtobeclickable(CheckoutPage.streetadd2)
        field.clear()
        field.send_keys(streetadd2)

    def streetadd3(self, streetadd3):
        field = self.elementtobeclickable(CheckoutPage.streetadd3)
        field.clear()
        field.send_keys(streetadd3)

    def city(self, city):
        field = self.elementtobeclickable(CheckoutPage.city)
        field.clear()
        field.send_keys(city)

    def state(self, state):
        select = Select(self.elementtobeclickable(CheckoutPage.state))
        select.select_by_visible_text(state)

    def zip(self, zip_code):
        field = self.elementtobeclickable(CheckoutPage.zip)
        field.clear()
        field.send_keys(zip_code)

    def country(self, country):
        select = Select(self.elementtobeclickable(CheckoutPage.country))
        select.select_by_visible_text(country)

    def phone(self, phone):
        field = self.elementtobeclickable(CheckoutPage.phone)
        field.clear()
        field.send_keys(phone)

    # ----------------- SHIPPING & PAYMENT -----------------
    def shipping_method(self):
        """Select shipping method."""
        self.elementtobeclickable(CheckoutPage.shipping_method).click()

    def nextbtn(self):
        """Click next button in checkout."""
        self.elementtobeclickable(CheckoutPage.nextbtn).click()

    def acknowledge(self):
        """Acknowledge terms and conditions."""
        self.elementtobeclickable(CheckoutPage.acknowledge).click()

    def placeorder(self):
        """Place the order."""
        self.elementtobeclickable(CheckoutPage.placeOrder).click()


