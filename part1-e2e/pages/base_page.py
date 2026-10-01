from playwright.sync_api import Page


class BasePage:
    path = "/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.locator("h1").first
        self.customer_menu = page.locator("#customer_menu_top")
        self.search_input = page.locator("#filter_keyword")
        self.search_btn = page.locator(".button-in-search")
        self.category_menu = page.locator("#categorymenu")

    def open(self):
        # relative to base_url set in browser_context_args
        self.page.goto(self.path)
        return self

    def search_for(self, keyword: str) -> None:
        self.search_input.fill(keyword)
        self.search_btn.click()

    def open_category(self, name: str) -> None:
        self.category_menu.get_by_role("link", name=name).first.click()
