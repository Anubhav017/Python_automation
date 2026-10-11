# Part 1 – Test Flows and Test Cases

**Website under test:** [Automation Test Store](https://automationteststore.com) – a public demo online shop (beauty, apparel, books).
**What is tested:** the four things a shopper does most – log in, find products, put them in the cart, and pay – plus a few edge cases on each (empty input, no results, changing and removing cart items).

## How to read this document
- A **test flow** is the journey a real shopper takes, written in plain words.
- A **test case** is one specific check inside that journey, with exact steps and the result we expect.
- Every test case has an **ID** (e.g. `TC-LOGIN-01`). The table below links each ID to its automated test, and the HTML report lists tests by that same file and function name, so anyone can match a report line to this page.

| Test case | Automated test (file::function) |
|---|---|
| TC-LOGIN-01 | `tests/test_login.py::test_login[valid_credentials]` |
| TC-LOGIN-02 | `tests/test_login.py::test_login[wrong_password]` |
| TC-LOGIN-03 | `tests/test_login.py::test_login[empty_fields]` |
| TC-SEARCH-01 | `tests/test_search.py::test_search_by_keyword` |
| TC-SEARCH-02 | `tests/test_search.py::test_search_by_category` |
| TC-SEARCH-03 | `tests/test_search.py::test_search_by_price_low_to_high` |
| TC-SEARCH-04 | `tests/test_search.py::test_search_with_no_results` |
| TC-CART-01 | `tests/test_cart.py::test_add_product_to_cart` |
| TC-CART-02 | `tests/test_cart.py::test_update_quantity_recalculates_total` |
| TC-CART-03 | `tests/test_cart.py::test_remove_product_empties_cart` |
| TC-CHECKOUT-01 | `tests/test_checkout.py::test_checkout_as_registered_customer` |

## Test data
**Login tests** use one fixed account, created once on the store. Its login name, password and first name are kept in `.env` (`LOGIN_NAME`, `LOGIN_PASSWORD`, `LOGIN_FIRST_NAME`), never in code; without them the login tests are skipped.

For **checkout**, which fills the cart, the tests **create a brand-new customer account** at the start of every run (name, address in Bangalore, India). The login name and email get a random suffix (e.g. `anu3f9a1c2b`), so runs never clash and can be repeated any number of times.

---

## Flow 1 – Login

**In plain words:** A customer who already has an account goes to the login page, types their login name and password, and lands on their "My Account" page.

| ID | Title | Steps | Expected result |
|---|---|---|---|
| TC-LOGIN-01 | Login with correct details | 1. Open the login page.<br>2. Enter the login name and password of the account created for this run.<br>3. Click **Login**. | The "My Account" page opens and the top bar says **"Welcome back <first name>"**. |
| TC-LOGIN-02 | Login with wrong password | 1. Open the login page.<br>2. Enter a valid login name and a wrong password.<br>3. Click **Login**. | The customer stays on the login page and sees the red message **"Incorrect login or password provided."** |
| TC-LOGIN-03 | Login with empty fields | 1. Open the login page.<br>2. Leave login name and password empty.<br>3. Click **Login**. | The customer stays on the login page and sees **"Incorrect login or password provided."** |

---

## Flow 2 – Searching products by three criteria

**In plain words:** A shopper finds products in three different ways: by typing a word, by picking a category from the menu, and by ordering products by price.

| ID | Criterion | Steps | Expected result |
|---|---|---|---|
| TC-SEARCH-01 | **By name (keyword)** | 1. Open the home page.<br>2. Type **shampoo** in the search box.<br>3. Click the search button. | A results page opens. At least one product is shown, and **every** product name contains the word "shampoo". |
| TC-SEARCH-02 | **By category** | 1. Open the home page.<br>2. Click **Makeup** in the top menu. | The Makeup category page opens with the heading "Makeup" and a list of products. |
| TC-SEARCH-03 | **By price** | 1. Open the **Makeup** category.<br>2. In "Sort By", choose **Price Low > High**. | The page reloads, and the product prices go from cheapest to most expensive (each price is the same as or higher than the one before it). |
| TC-SEARCH-04 | **No results** (edge case) | 1. Open the home page.<br>2. Search for a word no product has, **xyzqwe123**. | The page shows **"There is no product that matches the search criteria."** and no products. |

---

## Flow 3 – Adding products to the cart

**In plain words:** A shopper opens a product and clicks "Add to Cart". The product then shows up in their shopping cart.

| ID | Title | Steps | Expected result |
|---|---|---|---|
| TC-CART-01 | Add a product to the cart (guest) | 1. Search for **shampoo**.<br>2. Open the first product in the results.<br>3. Note the product name and the quantity on the page.<br>4. Click **Add to Cart**. | The Shopping Cart page opens. It has a row with the same product name and the same quantity. |
| TC-CART-02 | Change the quantity | 1. Add the first **shampoo** result to the cart.<br>2. Change its quantity to **3**.<br>3. Click **Update**. | The quantity shows 3 and the row total is **3 × unit price**. |
| TC-CART-03 | Remove the product | 1. Add the first **shampoo** result to the cart.<br>2. Click the trash icon on its row. | The cart shows **"Your shopping cart is empty!"** and the Checkout button is gone. |

---

## Flow 4 – Checkout

**In plain words:** A logged-in customer with a product in the cart goes to checkout, checks the order summary, confirms it, and gets an order number.

| ID | Title | Precondition | Steps | Expected result |
|---|---|---|---|---|
| TC-CHECKOUT-01 | Place an order as a registered customer | Customer is logged in and has a saved address (created during registration). | 1. Search for **shampoo** and open the first product.<br>2. Click **Add to Cart**.<br>3. In the cart, click **Checkout**.<br>4. On "Checkout Confirmation", check that the product is listed.<br>5. Click **Confirm Order**. | Step 4: the confirmation page lists the product.<br>Step 5: the page **"Your Order Has Been Processed!"** opens with the text **"Your order #<number> has been created!"** |

---

## Not automated (would add next)

These were left out on purpose: on a shared public demo store they depend on data or state we don't control and would make the suite flaky, or they need a second browser setup.

| Area | Case | Why not now |
|---|---|---|
| Login | Account locked after many failed logins | Would lock the shared run account and break the other tests |
| Search | Special characters and very long text in the search box (e.g. `<script>`, 500 chars) | Low risk for a demo; good fit for an API-level test |
| Search | Price filter at exact boundaries | Store prices change, so expected results aren't stable |
| Cart | Quantity 0, negative or non-numeric | Store behaviour is not specified, so there's no clear expected result |
| Cart | Out-of-stock product, minimum order quantity | Depends on stock levels we can't set |
| Checkout | Guest checkout, new address, invalid address fields | Longer flow; next in line after these |
| Checkout | Payment failure | The demo store has no real payment step |
| Session | Cart kept after logout/login, session timeout | Needs control over server session lifetime |
| Browsers | Firefox, WebKit, mobile viewport | One-line change in `pytest.ini` (`--browser`), but triples the run time on CI |

---

## For developers

- **Stack:** Python, Playwright, pytest, and pytest-html. The code uses the Page Object Model: `pages/` holds the locators and actions, and `tests/` holds the assertions.
- **No fixed sleeps.** Waiting comes from Playwright's auto-waiting and `expect(...)` checks (15 s timeout, set in `config.py`).
- **Login state.** The account is registered once per session through the UI. Its browser state is saved with `storage_state`, and the checkout test reuses it so it does not log in again (`conftest.py`).
- **On failure:** a screenshot, a video and a Playwright trace are kept in `test-results/`. Open a trace with `playwright show-trace test-results/<test>/trace.zip`.
- **Report:** `reports/report.html`, one self-contained file.

```bash
cd part1-e2e
pip install -r requirements.txt
playwright install chromium
pytest                   # all tests + HTML report
pytest -m smoke          # happy-path only
pytest --headed          # watch the browser
```
