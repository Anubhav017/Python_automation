from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout confirmation step; after confirming, the same heading locator shows the success page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.confirm_btn = page.locator("#checkout_btn")
        self.content = page.locator(".contentpanel").first

    def confirm_order(self) -> None:
        self.confirm_btn.click()
