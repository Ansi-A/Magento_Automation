import time

from selenium.webdriver import Keys

from utils.locators import CheckoutPage
from utils.locators import SelectItem
from pages.base_page import BasePage


class Item_Selection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # properly initializes self.driver

    def search(self, data):
        srh = self.elementtobeclickable(CheckoutPage.search)
        srh.click()
        srh.send_keys(data)
        srh.send_keys(Keys.ENTER)

    def item_select(self):

        self.visibilityofelement(CheckoutPage.itemselection).click()
    def item_size(self):
        self.elementtobeclickable(CheckoutPage.itemsize).click()
    def item_color(self):
        self.elementtobeclickable(CheckoutPage.itemcolor).click()

    def item_qty(self, quantity):
        qty_element = self.elementtobeclickable(CheckoutPage.itemqty)
        qty_element.click()
        qty_element.clear()  # clear input
        qty_element.send_keys(str(quantity))
        # enter quantity

    def checkout(self):
        self.elementtobeclickable(CheckoutPage.checkout).click()






