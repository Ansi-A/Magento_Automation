import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    wait = WebDriverWait(driver, 10)

    # Page objects
    login = LoginPage(driver)
    searcher = SearchItem(driver)
    selector = Item_Selection(driver)
    scroller = PageScroller(driver)
    checkout = CartCheckout(driver)

    # --- Login ---
    login.open_login()
    wait.until(lambda d: d.execute_script("return document.querySelector('[name=form_key]') !== null"))
    login.login_email("roni_cost@example.com")
    login.login_password("roni_cost3@example.com")

    login.login()

    # --- Search & Select Item ---
    searcher.search(test_data.search_data.item)
    scroller.scroll_to_bottom(4, 0.5)
    scroller.scroll_to_top(3, 0.5)
    time.sleep(1)
    selector.item_select()

    selector.item_size()
    selector.item_color()
    selector.item_qty(7)
    time.sleep(4)
    selector.checkout()
    checkout.shopping_cart()
    time.sleep(2)
    checkout.proceed_to_checkout()


    # --- Cart & Checkout ---

    driver.save_screenshot("screenshot_checkout.png")

    # --- Fill Checkout Form ---
    checkout.shipping_method()
    checkout.email = "salmmman@gmail.com"
    checkout.fname("Salman")
    checkout.lname("Zahid")
    checkout.company("OpenIntelX")
    checkout.streetadd1("Martian Town")
    checkout.streetadd2("Intel Road")
    checkout.streetadd3("Street no 6")
    checkout.city("New York")
    checkout.state("New York")
    checkout.zip("87439")
    checkout.country("Pakistan")
    checkout.phone("786753323")

    checkout.shipping_method()
    checkout.nextbtn()
    checkout.acknowledge()
    checkout.placeorder()

    # --- Verify Success ---
    wait.until(EC.url_contains("success"))
    driver.save_screenshot("screenshot_order_success.png")
