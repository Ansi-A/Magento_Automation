import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.base_page import BasePage
from tests import conftest
from utils import test_data


def test_login():
    driver = conftest.start()
    login= LoginPage(driver)
    base_page = BasePage(driver)


    # Wait dynamically until form_key is present
    login.open_login()
    login.login_email(test_data.UserData.email)
    login.login_password(test_data.UserData.password)
    login.login()