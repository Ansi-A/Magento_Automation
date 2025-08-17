import time

from selenium.webdriver import Keys

from utils.locators import CheckoutLocators
from pages.base_page import BasePage


class SearchItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # properly initializes self.driver

    def search(self, data):
        srh = self.elementtobeclickable(CheckoutLocators.SEARCH)
        srh.send_keys(data)
        srh.send_keys(Keys.ENTER)











