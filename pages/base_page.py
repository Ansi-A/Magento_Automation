from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def invisibilityofelement(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ec.invisibility_of_element_located(selector)
        )

    def url_checker(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            ec.url_contains(url)
        )

    def presenceofelementlocated(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
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

    def click(self, selector, timeout=10):
        el = self.elementtobeclickable(selector, timeout)
        el.click()

    def send_keys(self, selector, value, clear_first=True, timeout=10):
        el = self.visibilityofelement(selector, timeout)
        if clear_first:
            el.send_keys(Keys.CONTROL + 'a')
            el.send_keys(Keys.DELETE)
        el.send_keys(value)

    def select_by_visible_text(self, selector, visible_text, timeout=10):
        el = self.visibilityofelement(selector, timeout)
        select = Select(el)
        select.select_by_visible_text(visible_text)

    def wait_for_loader_to_disappear(self, timeout=10):
        loader_locator = (By.CSS_SELECTOR, "div.loading-mask[data-role='loader']")
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located(loader_locator)
            )
        except TimeoutException:
            pass

    def click_with_loader_wait(self, selector, timeout=10):
        element = self.elementtobeclickable(selector, timeout)
        self.wait_for_loader_to_disappear(timeout=5)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.wait_for_loader_to_disappear(timeout=3)
            element.click()

    def click_if_exists(self, selector, timeout=5):
        try:
            el = self.elementtobeclickable(selector, timeout)
            el.click()
            return True
        except TimeoutException:
            return False

    def fill_if_exists(self, selector, value, timeout=5, clear_first=True):
        try:
            el = self.visibilityofelement(selector, timeout)
            if clear_first:
                try:
                    el.clear()
                except Exception:
                    pass
            el.send_keys(value)
            return True
        except TimeoutException:
            return False

    def select_if_exists(self, selector, visible_text, timeout=5):
        try:
            el = self.visibilityofelement(selector, timeout)
            Select(el).select_by_visible_text(visible_text)
            return True
        except TimeoutException:
            return False
        except Exception:
            return False