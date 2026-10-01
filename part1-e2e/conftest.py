import re
from typing import Any

import pytest
from playwright.sync_api import Browser, Page, expect

import config
from pages.register_page import RegisterPage
from utils import data_factory

expect.set_options(timeout=config.EXPECT_TIMEOUT)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict[str, Any]) -> dict[str, Any]:
    args = {**browser_type_launch_args}
    if not config.HEADLESS:
        args["headless"] = False
    return args


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, Any]) -> dict[str, Any]:
    return {
        **browser_context_args,
        "base_url": config.BASE_URL,
        "viewport": {"width": 1366, "height": 768},
    }


@pytest.fixture(scope="session")
def registered_customer(browser: Browser, tmp_path_factory) -> dict[str, str]:
    # the store has no shared demo account, so register a fresh one once per session.
    # registration also logs the customer in, so we save that state for checkout tests
    customer = data_factory.build_customer()
    state_file = tmp_path_factory.mktemp("auth") / "auth.json"

    context = browser.new_context(base_url=config.BASE_URL)
    page = context.new_page()
    RegisterPage(page).open().register(customer)
    try:
        page.wait_for_url(re.compile(r"rt=account/success"), timeout=config.EXPECT_TIMEOUT)
    except Exception as e:
        raise RuntimeError(f"registration failed, still on {page.url}") from e
    context.storage_state(path=str(state_file))
    context.close()

    return {**customer, "state_file": str(state_file)}


@pytest.fixture
def logged_in_page(new_context, registered_customer: dict[str, str]) -> Page:
    context = new_context(storage_state=registered_customer["state_file"])
    return context.new_page()
