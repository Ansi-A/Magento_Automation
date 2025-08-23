# utils/locators.py
from selenium.webdriver.common.by import By

class CheckoutLocators:
    OPENLOGIN = (By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]")
    EMAIL = (By.NAME,"login[username]")
    PASSWORD = (By.NAME,"login[password]")
    LOGIN = (By.XPATH,"//fieldset[@class='fieldset login']//button[@id='send2']")
    SEARCH = (By.XPATH, "//input[@id='search']")
    SEARCHBTN = (By.XPATH,"//button[@title='Search']")
    ITEMSELECTION = (By.CSS_SELECTOR, "img[alt='Aether Gym Pant']")
    ITEMSIZE = (By.XPATH, "//div[@id='option-label-size-144-item-175']")
    ITEMCOLOR = (By.XPATH, "//div[@id='option-label-color-93-item-50']")
    ITEMQTY = (By.ID, "qty")
    CHECKOUT = (By.ID, "product-addtocart-button")
    NOCOUNTER = (By.XPATH,"//span[@class='counter-number']")
    SHOPPINGCART = (By.XPATH,"//a[normalize-space()='shopping cart']")
    PROCEEDTOCHECKOUT = (By.XPATH,"//button[@data-role='proceed-to-checkout']")
    EMAILID = (By.ID,"customer-email")
    SHIPPINGMETHOD = (By.XPATH,"//input[@type='radio' and @value='freeshipping_freeshipping']")
    FNAME = (By.NAME, "firstname")
    LNAME = (By.NAME, "lastname")
    COMPANY = (By.NAME, "company")
    STREETADD1 = (By.NAME, "street[0]")
    STREETADD2 = (By.NAME, "street[1]")
    STREETADD3 = (By.NAME, "street[2]")
    CITY = (By.NAME, "city")
    STATE = (By.NAME, "region")
    ZIP = (By.NAME, "postcode")
    COUNTRY = (By.NAME, "country_id")
    PHONE = (By.XPATH, "//input[@name='telephone']")
    SHIPPING_METHOD = (By.CSS_SELECTOR, "input[value='flatrate_flatrate']")
    NEXT0 = (By.XPATH,"//span[text()='Next']")
    NEXTBTN = (By.XPATH, "//button[@class='button action continue primary']")
    NEXT = (By.XPATH, "//span[normalize-space()='Next']")
    ACKNOWLEDGE = (By.ID, "billing-address-same-as-shipping-checkmo")
    PLACEORDER0 = (By.XPATH,"//span[text()='Place Order']")
    PLACEORDER = (By.XPATH, "//button[@title='Place Order']")


class REGISTRATIONPAGE:
    OPEN_REGISTRATION = (By.XPATH, "//a[contains(text(), 'Create an Account')]")
    FNAME = (By.ID, "firstname")
    LNAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRMPASSWORD = (By.ID, "password-confirmation")
    SUBMIT_CREATEACCOUNT = (By.CSS_SELECTOR, ".submit > span:nth-child(1)")


class SEARCHITEM:
    SEARCH_BOX = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@title='Search']")


class SELECTITEM:
    ITEMSELECTION = (By.XPATH, "//img[@alt='Hero Hoodie']")
    ITEMSIZE = (By.XPATH, "//div[@id='option-label-size-143-item-167']")
    ITEMCOLOR = (By.XPATH, "//div[@id='option-label-color-93-item-52']")
    ITEMQTY = (By.ID, "qty")
    CHECKOUT = (By.ID, "product-addtocart-button")


class ELEMENT_XPATH:
    CREATEACCOUNT = "//a[contains(text(), 'Create an Account')]"
    LOGINBTN = "//a[contains(text(),'Sign In')]"
    SUBMIT_LOGINBTN = "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"
    CHECKOUTNO1 = "//div[@data-role='loader']"
    CHECKOUTNO = "//span[@class='counter-number']"


class REGISTRATION_PAGE_ALT:
    REGISTRATION_PAGE = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    FNAME = (By.ID, "firstname")
    LNAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    LEMAIL = (By.ID, "email")
    LPASSWD = (By.ID, "pass")
    PASSWORD = (By.ID, "password")
    CONFIRMPASSWORD = (By.ID, "password-confirmation")
    CREATEACCOUNT = (By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")


class ID:
    SEARCH = "search"
    ITEMSIZESMALL = "option-label-size-143-item-167"
    ITEMCOLORGREY = "option-label-color-93-item-52"
    ITEMQTY = "qty"
    ADDTOCART = "product-addtocart-button"
    PROCEEDTOCHECKOUT = "top-cart-btn-checkout"


class CSS:
    SUBMIT_CREATEACCOUNT = ".submit > span:nth-child(1)"


class SHIPPING_ADDRESS:
    FNAME = "firstname"
    LNAME = "lastname"
    COMPANY = "company"
    STREETADD1 = "street[0]"
    STREETADD2 = "street[1]"
    STREETADD3 = "street[2]"
    CITY = "city"
    STATE = "region_id"
    ZIP = "postcode"
    COUNTRY = "country_id"
    PHONE = "//input[@name='telephone']"
    SHIPPING_METHOD = "input[value='flatrate_flatrate']"
    NEXT = "//button[@class='button action continue primary']"
    ACKNOWLEDGE = "//input[@id='billing-address-same-as-shipping-checkmo']"
    PLACEORDER = "//button[@title='Place Order']"
