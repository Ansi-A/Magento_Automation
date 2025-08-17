import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.base_page import BasePage
from tests import conftest

def test_login():
    driver = conftest.start()
    logger = LoginPage(driver)
    base_page = BasePage(driver)

    logger.open_login()

    # Wait dynamically until form_key is present
    WebDriverWait(driver, 5).until(
        lambda d: d.execute_script("return document.querySelector('[name=form_key]') !== null")
    )

    logger.login_email("harry9@gmail.com")
    logger.login_password("ui@Q.E@!e?w^Q2z")
    logger.login()

    time.sleep(5)  # optional to see result
