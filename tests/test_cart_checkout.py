import time
import pytest

from pages.login_page import LoginPage
from pages.search_item import SearchItem
from pages.item_select import Item_Selection
from pages.page_scroller import PageScroller
from pages.cart_checkout import CartCheckout
from tests import conftest
from utils import test_data


@pytest.mark.checkout
def test_checkout():
    driver = conftest.start()

    # Page objects
    login = LoginPage(driver)
    searcher = SearchItem(driver)
    selector = Item_Selection(driver)
    scroller = PageScroller(driver)
    checkout = CartCheckout(driver)

    # --- Login ---
    login.open_login()
    login.login_email(test_data.UserData.email)
    login.login_password(test_data.UserData.password)
    login.login()

    # --- Search & Select Item ---
    searcher.search(test_data.ItemData.search_term)
    scroller.scroll_to_bottom(1, 0.5)
    selector.select_item()

    selector.select_size()
    selector.select_color()
    selector.set_quantity(test_data.ItemData.quantity)
    selector.checkout()


    # --- Cart & Checkout ---
    checkout.shopping_cart()
    checkout.proceed_to_checkout()
    driver.save_screenshot("screenshot_checkout.png")

    # --- Fill Checkout Form ---
    checkout.shipping_method0()
    checkout.click_next()
    checkout.placeOrder0()
    time.sleep(2)

    checkout.email = test_data.CheckoutData.email
    checkout.fname(test_data.CheckoutData.first_name)
    checkout.lname(test_data.CheckoutData.last_name)
    checkout.company(test_data.CheckoutData.company)
    checkout.streetadd1(test_data.CheckoutData.street1)
    checkout.streetadd2(test_data.CheckoutData.street2)
    checkout.streetadd3(test_data.CheckoutData.street3)
    checkout.city(test_data.CheckoutData.city)
    checkout.state(test_data.CheckoutData.state)
    checkout.zip(test_data.CheckoutData.zip_code)
    checkout.country(test_data.CheckoutData.country)
    checkout.phone(test_data.CheckoutData.phone)

    checkout.shipping_method()
    checkout.nextbtn()
    checkout.acknowledge()
    checkout.placeorder()
