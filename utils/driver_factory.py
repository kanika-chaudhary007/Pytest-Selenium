"""
Isolated WebDriver creation. Tests and fixtures call create_driver()
and never construct a WebDriver directly, so browser/emulation setup
lives in exactly one place.

Only Chrome is implemented today (per assignment scope). Adding
Firefox/Edge later means adding a new _create_<browser>_driver()
function and one line in the dispatch dict below -- no existing
function needs to change.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from config.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


def _create_chrome_driver() -> webdriver.Chrome:
    """Create a Chrome WebDriver configured with mobile emulation from settings.json."""
    options = ChromeOptions()
    options.add_experimental_option("mobileEmulation", settings.mobile_emulation)

    if settings.headless:
        options.add_argument("--headless=new")

    options.add_argument("--disable-notifications")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    logger.info(
        "Chrome driver created (mobile_emulation=%s, headless=%s)",
        settings.mobile_emulation,
        settings.headless,
    )
    return driver


# Extension point: add "firefox": _create_firefox_driver, etc. when needed.
_BROWSER_FACTORIES = {
    "chrome": _create_chrome_driver,
}


def create_driver() -> webdriver.remote.webdriver.WebDriver:
    """
    Create and return a WebDriver instance for the browser configured
    in settings.json.

    Raises:
        ValueError: if the configured browser has no registered factory.
    """
    browser = settings.browser.lower()

    if browser not in _BROWSER_FACTORIES:
        logger.error("Unsupported browser configured: %s", browser)
        raise ValueError(
            f"Unsupported browser '{browser}'. "
            f"Supported: {list(_BROWSER_FACTORIES.keys())}"
        )

    return _BROWSER_FACTORIES[browser]()
