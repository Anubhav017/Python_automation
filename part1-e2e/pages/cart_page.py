from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/index.php?rt=checkout/cart"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.items_table = page.locator("table.table-striped").first
        self.checkout_btn = page.locator("#cart_checkout1")

    def row_for(self, product_name: str) -> Locator:
        return self.items_table.locator("tr", has_text=product_name)

    def quantity_for(self, product_name: str) -> Locator:
        return self.row_for(product_name).locator("input[name^='quantity']")

    def checkout(self) -> None:
        self.checkout_btn.click()
