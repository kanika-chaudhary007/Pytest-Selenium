"""
Page object for the Twitch search input and search results.
"""

from selenium.common.exceptions import ElementClickInterceptedException

from pages.base_page import BasePage
from locators import search_page_locators as loc
from utils import wait_utils
from utils.logger import get_logger

logger = get_logger(__name__)


class SearchPage(BasePage):
    """Interactions available once the search UI is open."""

    def search(self, term: str) -> None:
        """Type a search term into the search input."""
        self.type_text(loc.SEARCH_INPUT, term)
        logger.info("Searched for: %s", term)

    def scroll_results(self, times: int) -> None:
        """Scroll the search results page down `times` times."""
        self.scroll_down(times)

    def select_first_streamer(self) -> None:
        """
        Click the first streamer result in the results list.
        """
        results = wait_utils.wait_for_all_visible(
            self.driver,
            loc.STREAMER_RESULT_ITEMS
        )
        logger.info("Found %d streamer result(s)", len(results))

        first_result = results[0]

        try:
            first_result.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                first_result
            )
            self.driver.execute_script(
                "arguments[0].click();",
                first_result
            )

        logger.info("Selected first streamer result")