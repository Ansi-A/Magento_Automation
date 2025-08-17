from selenium.webdriver.common.by import By

class CheckoutPage():
    # Shipping / Billing locators
    openlogin=(By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]")
    email=(By.NAME,"login[username]")
    password=(By.NAME,"login[password]")
    login=(By.XPATH,"//fieldset[@class='fieldset login']//button[@id='send2']")
    search = (By.XPATH, "//input[@id='search']")
    searchbtn=(By.XPATH,"//button[@title='Search']")
    itemselection = (By.XPATH, "//img[@alt='Aether Gym Pant']")
    itemsize = (By.XPATH, "//div[@id='option-label-size-144-item-175']")
    itemcolor = (By.XPATH, "//div[@id='option-label-color-93-item-51']")
    itemqty = (By.ID, "qty")
    checkout = (By.ID, "product-addtocart-button")
    nocounter=(By.XPATH,"//span[@class='counter-number']")
    shoppingcart=(By.XPATH,"//a[normalize-space()='shopping cart']")
    proceedtocheckout=(By.XPATH,"//button[@data-role='proceed-to-checkout']")
    emailid=(By.XPATH,"//input[@id='customer-email']")
    shippingmethod=(By.XPATH,"//input[@type='radio' and @value='freeshipping_freeshipping']")
    fname = (By.NAME, "firstname")
    lname = (By.NAME, "lastname")
    company = (By.NAME, "company")
    streetadd1 = (By.NAME, "street[0]")
    streetadd2 = (By.NAME, "street[1]")
    streetadd3 = (By.NAME, "street[2]")
    city = (By.NAME, "city")
    state = (By.NAME, "region_id")
    zip = (By.NAME, "postcode")
    country = (By.NAME, "country_id")
    phone = (By.XPATH, "//input[@name='telephone']")
    shipping_method = (By.CSS_SELECTOR, "input[value='flatrate_flatrate']")
    nextbtn = (By.XPATH, "//button[@class='button action continue primary']")
    next=(By.XPATH, "//span[normalize-space()='Next']")
    acknowledge = (By.ID, "billing-address-same-as-shipping-checkmo")
    placeOrder = (By.XPATH, "//button[@title='Place Order']")

class RegistrationPage:
    # Locators
    open_registration = (By.XPATH, "//a[contains(text(), 'Create an Account')]")
    fname = (By.ID, "firstname")
    lname = (By.ID, "lastname")
    email = (By.ID, "email_address")
    password = (By.ID, "password")
    confirmPassword = (By.ID, "password-confirmation")
    submit_createAccount = (By.CSS_SELECTOR, ".submit > span:nth-child(1)")


class SearchItem:
    # Locators
    search_box = (By.ID, "search")
    search_button = (By.XPATH, "//button[@title='Search']")
class SelectItem:
    itemselection = (By.XPATH, "//img[@alt='Hero Hoodie']")
    itemsize = (By.XPATH, "//div[@id='option-label-size-143-item-167']")
    itemcolor=(By.XPATH, "//div[@id='option-label-color-93-item-52']")
    itemqty=(By.ID, "qty")
    checkout = (By.ID, "product-addtocart-button")



class element_Xpath:
    createAccount = "//a[contains(text(), 'Create an Account')]"
    LoginBtn = "//a[contains(text(),'Sign In')]"
    submit_LoginBtn="//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]"

    checkoutno1 = "//div[@data-role='loader']"
    checkoutno = "//span[@class='counter-number']"

class registeration_page:
    registeration_page = (By.XPATH, "//div[@class='panel header']//a[normalize-space()='Create an Account']")
    fname = (By.ID, "firstname")
    lname = (By.ID, "lastname")
    email = (By.ID, "email_address")
    lemail = (By.ID, "email")
    lpasswd = (By.ID, "pass")
    password = (By.ID, "password")
    confirmPassword = (By.ID, "password-confirmation")
    createAccount = (By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")


class ID:

    search = "search"
    itemsizesmall="option-label-size-143-item-167"
    itemcolorgrey="option-label-color-93-item-52"
    itemqty="qty"
    AddtoCart = "product-addtocart-button"
    proceedtocheckout = "top-cart-btn-checkout"

class CSS:
    Submit_createAccount = ".submit > span:nth-child(1)"
class Shipping_address:
    fname="firstname"
    lname="lastname"
    company="company"
    streetadd1="street[0]"
    streetadd2="street[1]"
    streetadd3="street[2]"
    city="city"
    state="region_id"
    zip="postcode"
    country="country_id"
    phone="//input[@name='telephone']"
    shipping_method="input[value='flatrate_flatrate']"
    next="//button[@class='button action continue primary']"
    acknowledge="//input[@id='billing-address-same-as-shipping-checkmo']"
    placeorder="//button[@title='Place Order']"