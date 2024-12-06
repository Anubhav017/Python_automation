import json
import logging
import pytest
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONFIG_PATH = "config.json"
DEFAULT_URL = "https://test.defyn3aqam6ot.amplifyapp.com/login"


@pytest.fixture(scope='function')
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope='function')
def config(request):
    env_option = request.config.getoption("--env")
    playwright_browser_option = request.config.getoption("--playwright-browser")

    with open(CONFIG_PATH, "r") as config_file:
        config_data = json.load(config_file)

    # Default to Chrome if not specified
    if playwright_browser_option not in ["chromium", "firefox", "webkit", "chrome"]:
        playwright_browser_option = config_data["environments"][env_option].get("browser", "chrome")

    config_data["environments"][env_option]["browser"] = playwright_browser_option

    return config_data["environments"].get(env_option, {})


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: test, staging, or dev")
    parser.addoption("--playwright-browser", action="store", default=None,
                     help="Browser for Playwright: chromium, firefox, webkit, or chrome")
    parser.addoption("--keep-browser-open", action="store_true", default=False,
                     help="Keep the browser open after tests")


@pytest.fixture(scope='function')
def url_setup(config):
    return config.get("base_url", DEFAULT_URL)


@pytest.fixture(scope='function')
def playwright_browser(playwright_instance, config, request):
    browser_name = config.get("browser", "chrome")  # Default to Chrome if not specified
    headless_mode = config.get("headless_mode", False)
    keep_browser_open = request.config.getoption("--keep-browser-open")

    if browser_name == "chrome":
        # Launch Google Chrome by specifying the "chrome" channel
        browser = playwright_instance.chromium.launch(channel="chrome", headless=headless_mode)
    elif browser_name == "chromium":
        # Launch Chromium
        browser = playwright_instance.chromium.launch(headless=headless_mode)
    elif browser_name == "firefox":
        browser = playwright_instance.firefox.launch(headless=headless_mode)
    elif browser_name == "webkit":
        browser = playwright_instance.webkit.launch(headless=headless_mode)
    else:
        raise ValueError(f"Unsupported browser name: {browser_name}")

    yield browser

    if not keep_browser_open:
        browser.close()


@pytest.fixture(scope='function')
def playwright_context_and_page(playwright_browser, url_setup, request):
    context = playwright_browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto(url_setup, timeout=120000)  # Timeout in millisecond

    yield context, page

    # Capture screenshot on test failure
    if request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(screenshot, name="Screenshot", attachment_type=AttachmentType.PNG)
        logger.error("Test failed. Screenshot attached.")

    context.close()
