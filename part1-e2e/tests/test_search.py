import re

import pytest
from playwright.sync_api import Page, expect

import config
from pages.search_page import SearchPage


@pytest.mark.smoke
def test_search_by_keyword(page: Page) -> None:
    search = SearchPage(page).open()
    search.search_for(config.SEARCH_KEYWORD)

    expect(page).to_have_url(re.compile(rf"rt=product/search.*keyword={config.SEARCH_KEYWORD}"))
    expect(search.product_names.first).to_be_visible()
    names = search.product_names.all_inner_texts()
    assert names, "no products found"
    for name in names:
        assert config.SEARCH_KEYWORD in name.lower(), f"'{name}' does not match '{config.SEARCH_KEYWORD}'"


def test_search_by_category(page: Page) -> None:
    search = SearchPage(page).open()
    search.open_category(config.CATEGORY)

    expect(page).to_have_url(re.compile(r"rt=product/category"))
    expect(search.heading).to_contain_text(config.CATEGORY, ignore_case=True)
    expect(search.product_names.first).to_be_visible()


def test_search_by_price_low_to_high(page: Page) -> None:
    search = SearchPage(page).open()
    search.open_category(config.CATEGORY)
    search.sort_by("Price Low > High")

    expect(search.prices.first).to_be_visible()
    prices = search.price_values()
    assert len(prices) > 1, "need at least two products to check the order"
    assert prices == sorted(prices), f"prices are not sorted low to high: {prices}"


def test_search_with_no_results(page: Page) -> None:
    search = SearchPage(page).open()
    search.search_for("xyzqwe123")

    expect(search.content).to_contain_text("There is no product that matches the search criteria.")
    expect(search.product_names).to_have_count(0)
