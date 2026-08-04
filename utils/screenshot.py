"""
Reusable screenshot capture. Any page object or test can call
take_screenshot() without knowing about file naming or save paths.
"""

from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger import get_logger
from utils.helper import timestamp

logger = get_logger(__name__)

_SCREENSHOTS_DIR = Path(__file__).parent.parent / "screenshots"


def take_screenshot(driver: WebDriver, name: str = "screenshot") -> Path:
    """
    Save a screenshot of the current browser state.

    Args:
        driver: active Selenium WebDriver instance.
        name: descriptive prefix for the filename (e.g. "streamer_page").

    Returns:
        Path to the saved screenshot file.
    """
    _SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{name}_{timestamp()}.png"
    filepath = _SCREENSHOTS_DIR / filename

    driver.save_screenshot(str(filepath))
    logger.info("Screenshot saved: %s", filepath)

    return filepath
