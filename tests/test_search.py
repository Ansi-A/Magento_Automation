from pages.page_scroller import PageScroller
from pages.search_item import SearchItem
import time
from utils import test_data

from tests import conftest


def test_search():
    driver=conftest.start()
    assert driver.current_url == "https://magento.softwaretestingboard.com/"
    searcher = SearchItem(driver)
    scroller = PageScroller(driver)
    searcher.search(test_data.search_data.item)
    scroller.scroll_to_bottom(4,.5)
    scroller.scroll_to_top(2,.5)
    time.sleep(5)