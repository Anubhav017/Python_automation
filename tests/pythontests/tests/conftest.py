import json
import time

import logging
import allure
import pytest
from allure_commons.types import AttachmentType
from utilities.driver_factory import DriverFactory


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 20
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]
DEFAULT_URL = "https://test.defyn3aqam6ot.amplifyapp.com/login"
DEFAULT_ENV = "dev"
cached_url = None


@pytest.fixture(scope='session')
def config(request):
    env_option = request.config.getoption("--env").strip().rstrip("\\")
    browser_option = request.config.getoption("--custom-browser").strip()
    with open(CONFIG_PATH, "r") as config_file:
        config_data = json.load(config_file)
    if browser_option in SUPPORTED_BROWSERS:
        config_data["environments"][env_option]["browser"] = browser_option
    return config_data.get("environments", {}).get(env_option, {})


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="dev and prod")
    parser.addoption("--custom-browser", action="store", default="chrome", help="chrome and edge")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env", default=DEFAULT_ENV)


@pytest.fixture(scope='session')
def browser_setup(request):
    browser = request.config.getoption("--custom-browser")
    if browser not in SUPPORTED_BROWSERS:
        raise Exception(f'"{browser}" is not a supported browser')
    return browser


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['timeout'] if 'timeout' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    global cached_url
    if cached_url is None:
        cached_url = config.get("base_url", DEFAULT_URL)
    return cached_url


@pytest.fixture()
def setup(request, config, url_setup):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed

    if config["browser"] == "chrome":
        driver.maximize_window()
        driver.get(url_setup)
        driver.set_page_load_timeout(config.get("page_load_timeout", 60))
        logger.info("Navigated to the URL in Chrome browser")

    elif config["browser"] == "edge":
        driver.maximize_window()
        driver.set_window_size(1280, 720)
        driver.get(url_setup)
        driver.set_page_load_timeout(60)
        logger.info("Navigated to the URL in Edge browser")

    yield
    if request.session.testsfailed != before_failed:
        logs = driver.get_log("browser")
        log_messages = "\n".join([f"{log['level']} - {log['message']}" for log in logs])
        allure.attach(log_messages, "Console Logs", attachment_type=AttachmentType.TEXT)
        allure.attach(driver.get_screenshot_as_png(), 'Screenshot', attachment_type=AttachmentType.PNG)
        logger.error("Test failed. Logs and screenshot attached.")

    time.sleep(3)
    # driver.quit()
