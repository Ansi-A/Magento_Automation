# base.py
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import TimeoutException

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

    # ---------- helpers that SKIP if element missing ----------
    def click_if_exists(self, selector, timeout=5):
        """Click the element if it becomes clickable; otherwise skip."""
        try:
            el = self.elementtobeclickable(selector, timeout)
            el.click()
            return True
        except TimeoutException:
            print(f"[INFO] Click skipped: {selector} not found/clickable.")
            return False

    def fill_if_exists(self, selector, value, timeout=5, clear_first=True):
        """Fill input if visible; otherwise skip."""
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
            print(f"[INFO] Fill skipped: {selector} not found/visible.")
            return False

    def select_if_exists(self, selector, visible_text, timeout=5):
        """Select by visible text if <select> exists; otherwise skip."""
        try:
            el = self.visibilityofelement(selector, timeout)
            Select(el).select_by_visible_text(visible_text)
            return True
        except TimeoutException:
            print(f"[INFO] Select skipped: {selector} not found/visible.")
            return False
        except Exception as e:
            print(f"[INFO] Select skipped: {selector} not a <select> or value '{visible_text}' not present. {e}")
            return False
