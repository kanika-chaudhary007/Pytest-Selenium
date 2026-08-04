"""
Locators for the streamer/channel page: modal dismissal and the
video player element used to determine "page fully loaded".

"""

from selenium.webdriver.common.by import By

# Mature-content warning modal, shown on some (not all) streams.
MATURE_CONTENT_ACCEPT_BUTTON = (By.CSS_SELECTOR, '[data-a-target="player-overlay-mature-accept"]')

# Cookie consent banner (OneTrust), shown site-wide on first visit.
COOKIE_CONSENT_ACCEPT_BUTTON = (By.CSS_SELECTOR, '#onetrust-accept-btn-handler')

# Video player -- presence/visibility of this is treated as "stream loaded".
VIDEO_PLAYER = (By.CSS_SELECTOR, '[data-a-target="video-player"]')

SEARCH_ICON = (By.XPATH, "(//div[contains(@role,'presentation')])[1]")

