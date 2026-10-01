from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/index.php?rt=account/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username = page.locator("#loginFrm_loginname")
        self.password = page.locator("#loginFrm_password")
        self.login_btn = page.locator("#loginFrm button[title='Login']")
        self.error_message = page.locator(".alert-danger")

    def login(self, user: str, pwd: str) -> None:
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
