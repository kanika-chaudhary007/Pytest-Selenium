# Twitch Mobile UI Automation

A scalable Selenium + Pytest automation framework that validates the Twitch mobile web search flow using Google Chrome Mobile Emulation.

## Test Scenario

The automated test performs the following steps:

1. Open Twitch
2. Click the Search icon
3. Search for **StarCraft II**
4. Scroll down twice
5. Select the first streamer
6. Wait for the streamer page to load
7. Handle any optional pop-up (if displayed)
8. Capture a screenshot

---

## Project Structure

```
UI-Automation/
│── config/          # Configuration files
│── locators/        # Page locators
│── pages/           # Page Object Model
│── resources/       # Test data
│── tests/           # Test cases
│── utils/           # Driver, waits, logger, screenshots
│── logs/            # Execution logs
│── reports/         # HTML reports
│── screenshots/     # Captured screenshots
│── conftest.py      # Pytest fixtures
│── requirements.txt
│── pytest.ini
```

---

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Chrome Mobile Emulation
- webdriver-manager
- pytest-html

---

## Framework Highlights

- Page Object Model (POM)
- Reusable utility classes
- Externalized configuration
- Explicit waits for stable execution
- Logging and screenshot support
- HTML test reports
- Easy to extend with new pages and test cases

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd UI-Automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest -v
```

---

## Test Output

After execution:

- Screenshot saved in `screenshots/`
- Logs generated in `logs/`
- HTML report available in `reports/`

---

## Design Principles

- Clear separation of locators, page objects, utilities, and tests.
- Driver setup managed through Pytest fixtures.
- Explicit waits used throughout the framework for reliable execution.
- Configuration stored outside the test code for easier maintenance.
- New pages and test cases can be added with minimal changes.

---
