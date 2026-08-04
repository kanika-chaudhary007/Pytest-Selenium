"""
Page object for the Twitch home/landing page.
"""

from pages.base_page import BasePage
from locators import home_page_locators as loc
from config.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    """Interactions available on the Twitch home page."""

    def load(self) -> None:
        """Navigate to the configured base URL."""
        self.driver.get(settings.base_url)
        print("Current URL:", self.driver.current_url)
        logger.info("Navigated to %s", settings.base_url)

    def open_search(self) -> None:
        """Click the search icon to reveal the search input."""
        self.click(loc.SEARCH_ICON)
