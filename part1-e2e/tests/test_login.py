import re

import pytest
from playwright.sync_api import Page, expect

import config
from pages.login_page import LoginPage

pytestmark = pytest.mark.skipif(
    not (config.LOGIN_NAME and config.LOGIN_PASSWORD), reason="LOGIN_NAME / LOGIN_PASSWORD not set in .env"
)


@pytest.mark.parametrize(
    ("login_name", "password", "should_succeed"),
    [
        pytest.param(config.LOGIN_NAME, config.LOGIN_PASSWORD, True, id="valid_credentials", marks=pytest.mark.smoke),
        pytest.param(config.LOGIN_NAME, "wrong-password", False, id="wrong_password"),
        pytest.param("", "", False, id="empty_fields"),
    ],
)
def test_login(page: Page, login_name: str, password: str, should_succeed: bool) -> None:
    login = LoginPage(page).open()
    login.login(login_name, password)

    if should_succeed:
        expect(page).to_have_url(re.compile(r"rt=account/account"))
        expect(login.heading).to_contain_text("My Account", ignore_case=True)
        expect(login.customer_menu).to_contain_text(f"Welcome back {config.LOGIN_FIRST_NAME}")
    else:
        expect(login.error_message).to_contain_text("Incorrect login or password provided.")
        expect(page).to_have_url(re.compile(r"rt=account/login"))
        expect(login.login_btn).to_be_visible()
