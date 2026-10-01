from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.name = self.heading
        self.quantity = page.locator("#product_quantity")
        self.add_to_cart_btn = page.locator("a.cart")

    def add_to_cart(self) -> None:
        self.add_to_cart_btn.click()
