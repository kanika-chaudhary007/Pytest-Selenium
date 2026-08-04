"""
Page object for an individual streamer/channel page.
"""

from pathlib import Path

from pages.base_page import BasePage
from locators import streamer_page_locators as loc
from utils import wait_utils
from utils.screenshot import take_screenshot
from utils.logger import get_logger

logger = get_logger(__name__)

# Candidate modals checked, in order, after landing on a streamer page.
_MODAL_LOCATORS = [
    loc.MATURE_CONTENT_ACCEPT_BUTTON,
    loc.COOKIE_CONSENT_ACCEPT_BUTTON,
]


class StreamerPage(BasePage):
    """Interactions available on an individual streamer's channel page."""

    def dismiss_modal_if_present(self, timeout: int | None = None) -> bool:
        """Dismiss a mature-content warning or cookie consent modal, if present."""
        return super().dismiss_modal_if_present(_MODAL_LOCATORS, timeout=timeout)

    def wait_until_loaded(self) -> None:
        """
        Wait until the stream is considered fully loaded
        """
        wait_utils.wait_for_visible(self.driver, loc.VIDEO_PLAYER)
        logger.info("Streamer page fully loaded (video player visible)")

    def capture_screenshot(self, name: str = "streamer_page") -> Path:
        """Take a screenshot of the current streamer page."""
        return take_screenshot(self.driver, name)
