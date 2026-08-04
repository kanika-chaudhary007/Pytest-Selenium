"""
Centralized explicit-wait helpers. Page objects call these instead of
constructing their own WebDriverWait/expected_conditions calls, so
every wait in the framework behaves consistently and there is exactly
one place to tune timeout/polling behavior.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from config.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


def wait_for_visible(driver: WebDriver, locator: tuple[By, str], timeout: int | None = None) -> WebElement:
    """Wait until the element located by `locator` is visible, then return it."""
    timeout = timeout or settings.timeouts.explicit
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        logger.error("Timed out waiting for element to be visible: %s", locator)
        raise


def wait_for_clickable(driver: WebDriver, locator: tuple[By, str], timeout: int | None = None) -> WebElement:
    """Wait until the element located by `locator` is clickable, then return it."""
    timeout = timeout or settings.timeouts.explicit
    try:
        return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    except TimeoutException:
        logger.error("Timed out waiting for element to be clickable: %s", locator)
        raise


def wait_for_all_visible(driver: WebDriver, locator: tuple[By, str], timeout: int | None = None) -> list[WebElement]:
    """Wait until all elements located by `locator` are visible, then return them."""
    timeout = timeout or settings.timeouts.explicit
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    except TimeoutException:
        logger.error("Timed out waiting for elements to be visible: %s", locator)
        raise


def wait_for_presence(driver: WebDriver, locator: tuple[By, str], timeout: int | None = None) -> WebElement:
    """Wait until the element located by `locator` is present in the DOM (not necessarily visible)."""
    timeout = timeout or settings.timeouts.explicit
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        logger.error("Timed out waiting for element to be present: %s", locator)
        raise


def is_present_within(driver: WebDriver, locator: tuple[By, str], timeout: int | None = None) -> bool:
    """
    Return True if the element appears within `timeout` seconds, False otherwise.
    Never raises. Intended for optional UI (e.g. modals) where absence is a valid state.
    """
    timeout = timeout if timeout is not None else settings.timeouts.modal
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False
