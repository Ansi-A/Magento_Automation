# base.py
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

    # ---------- NEW: CRITICAL METHODS (FAIL TEST IF MISSING) ----------
    def click(self, selector, timeout=10):
        """CLICK AN ELEMENT. IF IT FAILS, THE TEST FAILS."""
        el = self.elementtobeclickable(selector, timeout)
        el.click()
        print(f"✅ Clicked: {selector}")

    def send_keys(self, selector, value, clear_first=True, timeout=10):
        """FILL A FIELD. IF IT FAILS, THE TEST FAILS."""
        el = self.visibilityofelement(selector, timeout)
        if clear_first:
            el.send_keys(Keys.CONTROL + 'a')
            el.send_keys(Keys.DELETE)
        el.send_keys(value)
        print(f"✅ Filled {selector}: {value}")

    def select_by_visible_text(self, selector, visible_text, timeout=10):
        """SELECT FROM DROPDOWN. IF IT FAILS, THE TEST FAILS."""
        el = self.visibilityofelement(selector, timeout)
        select = Select(el)
        select.select_by_visible_text(visible_text)
        print(f"✅ Selected {selector}: {visible_text}")

    # ---------- NEW: LOADER HANDLING (For Magento) ----------
    def wait_for_loader_to_disappear(self, timeout=10):
        """
        Magento-specific method. Waits for the common loading overlay to disappear.
        """
        loader_locator = (By.CSS_SELECTOR, "div.loading-mask[data-role='loader']")
        try:
            print("⌛ Waiting for loader to disappear...")
            WebDriverWait(self.driver, timeout).until(
                ec.invisibility_of_element_located(loader_locator)
            )
            print("✅ Loader disappeared.")
        except TimeoutException:
            print("⚠️  Loader did not disappear, but continuing anyway.")
            # Don't raise an exception, just log it and continue.

    def click_with_loader_wait(self, selector, timeout=10):
        """
        A robust click method that waits for loaders to disappear before clicking.
        Use this for any click action in Magento.
        """
        # First, wait for the element to be clickable
        element = self.elementtobeclickable(selector, timeout)

        # Second, wait for any loader to disappear
        self.wait_for_loader_to_disappear(timeout=5)

        # Finally, attempt to click
        try:
            element.click()
            print(f"✅ Clicked: {selector}")
        except ElementClickInterceptedException:
            # If still intercepted, one more wait and retry
            print("🔄 Click intercepted. Waiting once more for loader...")
            self.wait_for_loader_to_disappear(timeout=3)
            element.click()
            print(f"✅ Clicked on retry: {selector}")

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