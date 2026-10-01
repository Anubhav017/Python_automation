import re

import pytest
from playwright.sync_api import Page, expect

import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.mark.smoke
def test_checkout_as_registered_customer(logged_in_page: Page) -> None:
    page = logged_in_page
    search = SearchPage(page).open()
    search.search_for(config.SEARCH_KEYWORD)
    search.open_first_product()

    product = ProductPage(page)
    expect(product.add_to_cart_btn).to_be_visible()
    name = product.name.inner_text().strip()
    product.add_to_cart()

    cart = CartPage(page)
    expect(cart.row_for(name)).to_be_visible()
    cart.checkout()

    checkout = CheckoutPage(page)
    expect(page).to_have_url(re.compile(r"rt=checkout/confirm"))
    expect(checkout.heading).to_contain_text("Checkout Confirmation", ignore_case=True)
    expect(checkout.content).to_contain_text(name, ignore_case=True)
    checkout.confirm_order()

    expect(page).to_have_url(re.compile(r"rt=checkout/success"))
    expect(checkout.heading).to_contain_text("Your Order Has Been Processed!", ignore_case=True)
    expect(checkout.content).to_contain_text(re.compile(r"Your order #\d+ has been created"))
