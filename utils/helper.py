"""
Small generic helpers with no Selenium dependency, reusable anywhere
in the framework. Kept intentionally minimal: only functions with an
actual current caller live here.
"""

from datetime import datetime


def timestamp() -> str:
    """Return the current time as a filesystem-safe timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")
