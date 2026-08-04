"""
BasePage: generic, reusable browser interactions shared by every page
object. Deliberately minimal -- no business logic, no knowledge of
what any specific page contains. Page objects extend this and add
their own page-specific methods.
"""
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

from utils import wait_utils
from utils.logger import get_logger

logger = get_logger(__name__)

Locator = tuple[By, str]


class BasePage:
    """Common browser actions available to every page object."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def click(self, locator: Locator) -> None:
        """Wait for an element to be clickable, then click it."""
        element = wait_utils.wait_for_clickable(self.driver, locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            # Fallback for elements obscured by animations/overlays.
            self.driver.execute_script("arguments[0].click();", element)
        logger.info("Clicked element: %s", locator)

    def type_text(self, locator: Locator, text: str) -> None:
        """Wait for an input to be visible, clear it, and type text into it."""
        element = wait_utils.wait_for_visible(self.driver, locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
        logger.info("Typed %r into element: %s", text, locator)

    def get_text(self, locator: Locator) -> str:
        """Wait for an element to be visible and return its text."""
        element = wait_utils.wait_for_visible(self.driver, locator)
        return element.text

    def scroll_down(self, times: int = 1) -> None:
        """Scroll the viewport down by one screen height, `times` times."""
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

        logger.info("Scrolled down %d time(s)", times)

    def is_present(self, locator: Locator, timeout: int | None = None) -> bool:
        """Return True if the element appears within `timeout` seconds."""
        return wait_utils.is_present_within(self.driver, locator, timeout)

    def dismiss_modal_if_present(self, modal_locators: list[Locator], timeout: int | None = None) -> bool:
        """ Returns:True if a modal was found and dismissed, False otherwise. """
        
        for locator in modal_locators:
            if self.is_present(locator, timeout=timeout):
                self.click(locator)
                logger.info("Dismissed modal via locator: %s", locator)
                return True

        logger.info("No modal present (checked %d locator(s))", len(modal_locators))
        return False
