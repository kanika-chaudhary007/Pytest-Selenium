"""
End-to-end test: search Twitch for a game, open a streamer, and
capture a screenshot once the stream has loaded.

"""

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

import time
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from resources.test_data import SEARCH_TERMS
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.parametrize("search_term", SEARCH_TERMS)
def test_search_and_open_streamer(driver: WebDriver, search_term: str) -> None:
    """
    Search Twitch for `search_term`, open the first streamer result,
    handle any modal, and confirm the stream loads (screenshot proves it).
    """
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    streamer_page = StreamerPage(driver)

    #go to Twitch
    home_page.load()
    assert driver.current_url == "https://m.twitch.tv" or driver.current_url == "https://m.twitch.tv/", "Correct url not found"

    #click in the search icon
    home_page.open_search()

    #input StarCraft II
    search_page.search(search_term)

    time.sleep(1)    
    #scroll down 2 times
    search_page.scroll_results(times=2)

    time.sleep(1)  

    assert driver.current_url == "https://m.twitch.tv/search?term=StarCraft%20II", "User is not present on Starcraft II url"

    #Select one streamer
    search_page.select_first_streamer()

    streamer_page.dismiss_modal_if_present()

    #on the streamer page wait until all is load and take a screenshot
    streamer_page.wait_until_loaded()

    screenshot_path = streamer_page.capture_screenshot(name=f"streamer_{search_term.replace(' ', '_')}")

    assert screenshot_path.exists(), f"Expected screenshot at {screenshot_path}, but it was not created"
    assert screenshot_path.stat().st_size > 0, "Screenshot file was created but is empty"

    logger.info("Test completed successfully for search term: %s", search_term)
