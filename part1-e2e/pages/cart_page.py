from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/index.php?rt=checkout/cart"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.items_table = page.locator("table.table-striped").first
        self.checkout_btn = page.locator("#cart_checkout1")
        self.update_btn = page.locator("#cart_update")
        self.content = page.locator(".contentpanel").first

    def row_for(self, product_name: str) -> Locator:
        return self.items_table.locator("tr", has_text=product_name)

    def quantity_for(self, product_name: str) -> Locator:
        return self.row_for(product_name).locator("input[name^='quantity']")

    def unit_price_for(self, product_name: str) -> Locator:
        # columns: image, name, model, unit price, quantity, total, remove
        return self.row_for(product_name).locator("td").nth(3)

    def total_for(self, product_name: str) -> Locator:
        return self.row_for(product_name).locator("td").nth(5)

    def update_quantity(self, product_name: str, quantity: int) -> None:
        self.quantity_for(product_name).fill(str(quantity))
        self.update_btn.click()

    def remove(self, product_name: str) -> None:
        self.row_for(product_name).locator("a[href*='remove=']").click()

    def checkout(self) -> None:
        self.checkout_btn.click()
