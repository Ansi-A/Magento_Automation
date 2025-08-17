
from tests import conftest
import time
from pages.registration_page import RegistrationPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utils import *
import pytest

def test_registration_page():

    driver = conftest.start()
    time.sleep(1)
    reg_page = RegistrationPage(driver)
    reg_page.open_registration_page()
    reg_page.fname("Muhammad")
    reg_page.lname("Salmann")
    reg_page.email("salmmmman@gmail.com")
    reg_page.password("kaisaB12")
    reg_page.confirmPassword("kaisaB12")
    reg_page.Submit_createAccount()
    time.sleep(6)



