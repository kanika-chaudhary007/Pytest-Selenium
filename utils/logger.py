"""
Centralized logging configuration. Every module that needs to log
imports get_logger(__name__) instead of configuring logging itself,
so log format/level stays consistent across the whole framework.

Logs go to both the console (for live feedback while a test runs)
and a single timestamped file under logs/ (so a full execution trace
is available afterward without rerunning the suite -- useful for
debugging flaky runs and for evaluators reviewing a submission).
"""

import logging
import sys
from pathlib import Path

from utils.helper import timestamp

_LOGS_DIR = Path(__file__).parent.parent / "logs"
_FORMATTER = logging.Formatter(
    fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# One log file per process (e.g. per pytest run), shared by every
# logger created via get_logger() so the whole run lands in one file.
_LOG_FILE_PATH: Path | None = None


def _get_log_file_path() -> Path:
    """Lazily create the logs/ dir and pick one timestamped file for this run."""
    global _LOG_FILE_PATH
    if _LOG_FILE_PATH is None:
        _LOGS_DIR.mkdir(parents=True, exist_ok=True)
        _LOG_FILE_PATH = _LOGS_DIR / f"run_{timestamp()}.log"
    return _LOG_FILE_PATH


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger for the given module name.

    Safe to call multiple times for the same name (e.g. across test
    reruns within one pytest session) without duplicating handlers.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(_FORMATTER)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler(_get_log_file_path(), encoding="utf-8")
        file_handler.setFormatter(_FORMATTER)
        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        logger.propagate = False

    return logger
