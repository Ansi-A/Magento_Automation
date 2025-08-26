
from tests import conftest
import time
from pages.registration_page import RegistrationPage
from utils import test_data


def test_registration_page():

    driver = conftest.start()
    time.sleep(1)
    reg_page = RegistrationPage(driver)
    reg_page.open_registration_page()
    reg_page.fname(test_data.UserData.fname)
    reg_page.lname(test_data.UserData.lname)
    reg_page.email(test_data.UserData.email)
    reg_page.password(test_data)
    reg_page.confirm_password(test_data.UserData.password)
    reg_page.submit_create_account()
    time.sleep(6)



