from playwright.sync_api import Page

from pages.base_page import BasePage


class SearchPage(BasePage):
    """Product listing: keyword search results and category pages share this layout."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # the store renders grid and list views at once, :visible keeps only the shown one.
        # "prdocutname" is the store's own (misspelled) class name
        self.product_names = page.locator(".prdocutname:visible")
        self.prices = page.locator(".thumbnails .oneprice:visible, .thumbnails .pricenew:visible")
        self.sort_select = page.locator("#sort")

    def sort_by(self, label: str) -> None:
        # changing the sort reloads the page
        with self.page.expect_navigation():
            self.sort_select.select_option(label=label)

    def price_values(self) -> list[float]:
        return [float(t.strip().lstrip("$").replace(",", "")) for t in self.prices.all_inner_texts()]

    def open_first_product(self) -> None:
        self.product_names.first.click()
