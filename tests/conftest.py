import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils.test_data import target_info


def start(max_retries=3, retry_delay=2):
    options = Options()
    options.binary_location = '/usr/bin/brave-browser'  # Update with your Brave path

    driver = None  # Initialize driver

    for attempt in range(1, max_retries + 1):
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(target_info.URL)
            driver.maximize_window()

            if (driver.current_url == target_info.URL and
                    "cloudflare" not in driver.page_source.lower()):
                return driver

            print(f"Retry {attempt}/{max_retries}...")
            time.sleep(retry_delay)

        except Exception as e:
            print(f"Attempt {attempt} failed: {str(e)}")
            if driver:  # Only quit if driver was created
                driver.quit()

    return None  # Explicit return None if all retries fail