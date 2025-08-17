from pages.page_scroller import PageScroller
from pages.item_select import Item_Selection

from pages.search_item import SearchItem
import time
from utils import test_data

from tests import conftest


def test_item_selector():
    driver=conftest.start()
    searcher = SearchItem(driver)
    selector = Item_Selection(driver)
    scroller = PageScroller(driver)
    searcher.search(test_data.search_data.item)
    scroller.scroll_to_bottom(4,.5)
    scroller.scroll_to_top(2,.5)
    selector.item_select()
    selector.item_size()
    selector.item_color()
    selector.item_qty(4)
    selector.checkout()
    time.sleep(5)