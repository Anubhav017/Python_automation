import re

import pytest
from playwright.sync_api import Page, expect

import config
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


def _add_first_search_result_to_cart(page: Page) -> str:
    search = SearchPage(page).open()
    search.search_for(config.SEARCH_KEYWORD)
    search.open_first_product()

    product = ProductPage(page)
    expect(product.add_to_cart_btn).to_be_visible()
    name = product.name.inner_text().strip()
    product.add_to_cart()
    return name


def _money(text: str) -> float:
    return float(text.strip().lstrip("$").replace(",", ""))


@pytest.mark.smoke
def test_add_product_to_cart(page: Page) -> None:
    search = SearchPage(page).open()
    search.search_for(config.SEARCH_KEYWORD)
    search.open_first_product()

    product = ProductPage(page)
    expect(product.add_to_cart_btn).to_be_visible()
    name = product.name.inner_text().strip()
    quantity = product.quantity.input_value()
    product.add_to_cart()

    cart = CartPage(page)
    expect(page).to_have_url(re.compile(r"rt=checkout/cart"))
    expect(cart.heading).to_contain_text("Shopping Cart", ignore_case=True)
    expect(cart.row_for(name)).to_be_visible()
    expect(cart.quantity_for(name)).to_have_value(quantity)


def test_update_quantity_recalculates_total(page: Page) -> None:
    name = _add_first_search_result_to_cart(page)
    cart = CartPage(page)
    expect(cart.row_for(name)).to_be_visible()
    unit_price = _money(cart.unit_price_for(name).inner_text())

    cart.update_quantity(name, 3)

    expect(cart.quantity_for(name)).to_have_value("3")
    expect(cart.total_for(name)).to_have_text(f"${unit_price * 3:,.2f}")


def test_remove_product_empties_cart(page: Page) -> None:
    name = _add_first_search_result_to_cart(page)
    cart = CartPage(page)
    expect(cart.row_for(name)).to_be_visible()

    cart.remove(name)

    expect(cart.content).to_contain_text("Your shopping cart is empty!")
    expect(cart.checkout_btn).to_be_hidden()
