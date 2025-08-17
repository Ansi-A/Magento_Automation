import time

class PageScroller:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_bottom(self, num, delay):
        for i in range(num):
            self.driver.execute_script("window.scrollBy(0,500);")
            time.sleep(delay)
    def scroll_to_top(self, num, delay):
        for i in range(num):
            self.driver.execute_script("window.scrollBy(0,-500);")
            time.sleep(delay)




