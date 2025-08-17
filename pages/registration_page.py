
from utils.locators import registeration_page
from pages.base_page import BasePage  # adjust path if needed

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_registration_page(self):
        self.elementtobeclickable(registeration_page.registeration_page).click()

    def fname(self, fname):
        self.visibilityofelement(registeration_page.fname).send_keys(fname)

    def lname(self, lname):
        self.visibilityofelement(registeration_page.lname).send_keys(lname)

    def email(self, email):
        self.visibilityofelement(registeration_page.email).send_keys(email)

    def password(self, password):
        self.visibilityofelement(registeration_page.password).send_keys(password)

    def confirmPassword(self, confirmPassword):
        self.visibilityofelement(registeration_page.confirmPassword).send_keys(confirmPassword)

    def Submit_createAccount(self):
        self.elementtobeclickable(registeration_page.createAccount).click()

