"""
Shared pytest fixtures. Driver creation and teardown live here only --
test files never construct a WebDriver directly.
"""

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.driver_factory import create_driver
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture
def driver() -> WebDriver:
    """
    Provide a fresh WebDriver instance per test, configured per
    settings.json (browser, mobile emulation, timeouts).

    Yields the driver for the test to use, then guarantees cleanup
    (driver.quit()) even if the test fails or raises.
    """
    logger.info("Setting up WebDriver for test")
    drv = create_driver()

    yield drv

    logger.info("Tearing down WebDriver")
    drv.quit()
