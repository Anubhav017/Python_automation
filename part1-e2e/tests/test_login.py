import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page, registered_customer: dict[str, str]) -> None:
    login = LoginPage(page).open()
    login.login(registered_customer["login_name"], registered_customer["password"])

    expect(page).to_have_url(re.compile(r"rt=account/account"))
    expect(login.heading).to_contain_text("My Account", ignore_case=True)
    expect(login.customer_menu).to_contain_text(f"Welcome back {registered_customer['first_name']}")


def test_login_with_wrong_password(page: Page, registered_customer: dict[str, str]) -> None:
    login = LoginPage(page).open()
    login.login(registered_customer["login_name"], "wrong-password")

    expect(login.error_message).to_contain_text("Incorrect login or password provided.")
    expect(page).to_have_url(re.compile(r"rt=account/login"))
    expect(login.login_btn).to_be_visible()
