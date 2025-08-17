# base.py
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def invisibilityofelement(self, selector, timeout=10):
        return WebDriverWait(self.driver,timeout).until(
            ec.invisibility_of_element_located(selector)
        )
    def url_checker(self,url):
        return WebDriverWait(self.driver,timeout=10).until(
            ec.url_contains(url)
        )




    def presenceofelementlocated(self, selector, timeout=10):
        return WebDriverWait(self.driver,timeout).until(
            ec.presence_of_element_located(selector)
        )

    def visibilityofelement(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(selector)
        )

    def elementtobeclickable(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(selector)
        )


