from pages.base_page import BasePage
from pages.cart_checkout import CartCheckout
from pages.item_select import Item_Selection
from pages.login_page import LoginPage
from pages.page_scroller import PageScroller
from pages.search_item import SearchItem
from tests import conftest
from utils import test_data


def test_checkout():
    driver = conftest.start()
    page = BasePage(driver)
    log =page.get_logger()

    log.info("Browser opened")

    # Page objects
    login = LoginPage(driver)
    searcher = SearchItem(driver)
    selector = Item_Selection(driver)
    scroller = PageScroller(driver)
    checkout = CartCheckout(driver)

    # --- Login
    try:
        log.info("Login Page opened")
        login.open_login()
        login.login_email(test_data.UserData.email)
        log.info("Email Filled")
        login.login_password(test_data.UserData.password)
        log.info("Password Filled")
        login.login()
        log.info("Logged in successfully")
    except Exception as error:
        log.exception(f"Error occurred during login {error}")


        # --- Search & Select Item ---
    try:
        log.info("Search Page opened")
        searcher.search(test_data.search_data.item)
        log.info("Item Search Page opened")
        scroller.scroll_to_bottom(1, 0.5)
        selector.select_item()
        log.info("Item Selected")
        selector.select_size()
        log.info("Item size Selected")
        selector.select_color()
        log.info("Item color Selected")
        selector.set_quantity(test_data.ItemData.quantity)
        log.info("Item quantity Selected")
        selector.checkout()
        log.info("Item check out Successful")
    except Exception as error:
        log.exception(f"Error occurred during item search/selection:{error}")


    # --- Cart & Checkout ---
    try:
        checkout.shopping_cart()
        log.info("Shopping Cart Opened")
        checkout.proceed_to_checkout()
        log.info("Proceeded to checkout")
    except Exception as error:

        log.exception(f"Error occurred while opening cart/checkout: {error}")


    # --- DETECT CHECKOUT FLOW TYPE ---
    is_guest_flow = checkout.is_guest_checkout_flow()

    if is_guest_flow:
        # --- GUEST CHECKOUT FLOW ---
        try:
            log.info("Guest Checkout Flow Opened")
            checkout.email_id(test_data.CheckoutData.email)
            log.info("Guest Checkout Flow Email Filled")
            checkout.fname(test_data.CheckoutData.first_name)
            log.info("Guest Checkout First Name Filled")
            checkout.lname(test_data.CheckoutData.last_name)
            log.info("Guest Checkout Last Name Filled")
            checkout.company(test_data.CheckoutData.company)
            log.info("Guest Checkout Company Filled")
            checkout.streetadd1(test_data.CheckoutData.street1)
            log.info("Guest Checkout Street 1 Filled")
            checkout.streetadd2(test_data.CheckoutData.street2)
            log.info("Guest Checkout Street 2 Filled")
            #checkout.streetadd3(test_data.CheckoutData.street3)
            checkout.country(test_data.CheckoutData.country)
            log.info("Guest Checkout Country Filled")
            checkout.city(test_data.CheckoutData.city)
            log.info("Guest Checkout City Filled")
            checkout.state(test_data.CheckoutData.state)
            log.info("Guest Checkout State Filled")
            checkout.zip(test_data.CheckoutData.zip_code)
            log.info("Guest Checkout Zip Code Filled")
            checkout.phone(test_data.CheckoutData.phone)
            log.info("Guest Checkout Phone Filled")
            checkout.shipping_method()
            log.info("Guest Checkout Shipping Method selected")
            checkout.nextbtn()
            log.info("Guest Checkout Next btn selected")
            checkout.placeorder()
            log.info("Guest Checkout Order placed")
        except Exception as error:
            log.exception(f"Error occurred during guest checkout flow:{error}")


    else:
        # --- LOGGED-IN USER CHECKOUT FLOW ---
        try:
            log.info("Logged in User Flow entered")
            checkout.shipping_method0()
            log.info("Shipping method selected")
            checkout.click_next()
            log.info("Next button clicked")
            checkout.placeOrder0()
            log.info("Order placed")
        except Exception as error:
            log.exception(f"Error occurred during logged-in user checkout flow:{error}")

