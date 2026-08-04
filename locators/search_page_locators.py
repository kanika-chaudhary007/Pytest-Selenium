"""Locators for the Twitch search input and search results page.
"""

from selenium.webdriver.common.by import By


SEARCH_INPUT = (By.XPATH, "//input[@type='search']")


# Individual streamer result cards/links in the results list.
STREAMER_RESULT_ITEMS = (By.XPATH, "//button[contains(@class,'ScCoreLink')]")
