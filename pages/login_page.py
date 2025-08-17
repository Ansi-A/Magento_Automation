
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from tests import conftest
import time
from utils.locators import CheckoutPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # properly initializes self.driver

    def open_login(self):
        self.visibilityofelement(CheckoutPage.openlogin).click()


    def login_email(self, email):
        self.presenceofelementlocated(CheckoutPage.email).send_keys(email)

    def login_password(self, password):
        self.visibilityofelement(CheckoutPage.password).send_keys(password)
    def login(self):
        self.elementtobeclickable(CheckoutPage.login).click()


