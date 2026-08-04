"""
Loads configuration from settings.json and exposes it as a simple,
importable object. Intentionally flat: one file, one loader, no
provider/strategy abstraction, since a single JSON source is all
this project currently needs.
"""

import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, Any

_SETTINGS_PATH = Path(__file__).parent / "settings.json"


@dataclass(frozen=True)
class Timeouts:
    explicit: int
    modal: int


@dataclass(frozen=True)
class Config:
    base_url: str
    browser: str
    headless: bool
    timeouts: Timeouts
    mobile_emulation: Dict[str, Any] = field(default_factory=dict)


def _load_config() -> Config:
    """Read settings.json once at import time and return a Config instance."""
    with open(_SETTINGS_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    return Config(
        base_url=raw["base_url"],
        browser=raw["browser"],
        headless=raw["headless"],
        timeouts=Timeouts(**raw["timeouts"]),
        mobile_emulation=raw["mobile_emulation"],
    )


# Single shared config instance, imported wherever settings are needed:
#   from config.config import settings
settings = _load_config()
