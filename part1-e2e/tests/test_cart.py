import re

import pytest
from playwright.sync_api import Page, expect

import config
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


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
