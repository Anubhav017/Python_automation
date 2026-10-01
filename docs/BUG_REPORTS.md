# Bug Reports

## BUG-001 – Product page pre-fills quantity "2", so the cart total is doubled

| Field | Value |
|---|---|
| **Area** | Product page → Shopping cart |
| **Severity** | Medium (the customer can be charged for more items than intended) |
| **Priority** | Medium |
| **Environment** | https://automationteststore.com, Chrome (Playwright Chromium), Windows 11, 2026-10-01 |
| **Status** | Open, needs confirmation from the product owner |

**Summary**
The product "Benefit Bella Bamba" opens with **2** already in the quantity box. A shopper who just clicks "Add to Cart" gets 2 items: the unit price is $28.00 and the cart total is $56.00.

**Steps to reproduce**
1. Open https://automationteststore.com/index.php?rt=product/product&product_id=52
2. Look at the quantity box. Do not change it.
3. Click **Add to Cart**.

**Expected result**
The quantity starts at 1. If the product has a minimum order of 2, the page clearly says so next to the quantity box.

**Actual result**
The quantity box shows 2. The cart has quantity 2 and a total of $56.00 for a $28.00 product.

**Evidence**
Seen during an automated run: the product page quantity was `2`, and the cart row showed `$28.00 … $56.00`.

**Note for developers**
Check whether a minimum quantity is configured for product 52. If it is intended, show a "Minimum quantity: 2" hint. If it is not, reset the default to 1.

---

## BUG-002 – Misspelled CSS class `prdocutname` on product listings

| Field | Value |
|---|---|
| **Area** | Search results and category pages (front-end markup) |
| **Severity** | Low (shoppers do not see it) |
| **Priority** | Low |
| **Environment** | https://automationteststore.com, all browsers |
| **Status** | Open |

**Summary**
The product name links on listing pages use the class `prdocutname` instead of `productname`.

**Steps to reproduce**
1. Search for "shampoo".
2. Inspect a product name in the results (right-click → Inspect).

**Expected result**
The class is spelled `productname`, which matches the product page.

**Actual result**
The class is `prdocutname`.

**Impact**
Styling and test selectors that use the correct spelling silently match nothing. Our own first test draft with `.productname` found zero products for this reason. Fixing the class name will break any selector that relies on the typo, so the change must be coordinated with the test team.

---

## Part 2 – API (Nominatim)

All three were reproduced on 2026-10-01 against https://nominatim.openstreetmap.org (software 5.3.0). Each one has an `xfail` test in `part2-api/tests` that will start passing once the bug is fixed.

## BUG-API-001 – Empty search query returns 200 instead of 400

| Field | Value |
|---|---|
| **Endpoint** | `GET /search` |
| **Severity** | Low |
| **Test** | `test_search.py::test_search_empty_query_returns_400` |

**Steps**
1. `GET /search?q=&format=json`
2. `GET /search?format=json` (no `q` at all), for comparison

**Expected result**
Both requests are rejected the same way: 400 `{"error": {"code": 400, "message": "Nothing to search for."}}`

**Actual result**
1. 200 OK with body `[]`
2. 400 "Nothing to search for."

**Impact**
A client cannot tell "nothing found" apart from "you sent nothing". A form that submits a blank search box looks like a search that found no results.

---

## BUG-API-002 – Out-of-range latitude returns 200 instead of 400

| Field | Value |
|---|---|
| **Endpoint** | `GET /reverse` |
| **Severity** | Medium |
| **Test** | `test_reverse.py::test_reverse_out_of_range_latitude_returns_400` |

**Steps**
1. `GET /reverse?lat=999&lon=77.5946&format=json`

**Expected result**
400 with a message such as "Parameter 'lat' must be between -90 and 90". Missing parameters already get a 400 (`Parameter 'lon' missing.`).

**Actual result**
200 OK with `{"error": "Unable to geocode"}`. This is the same response as a valid point in the open ocean (`lat=0&lon=-160`).

**Impact**
Invalid input looks like a successful call. Clients that only check the status code treat it as success, and a bad coordinate cannot be told apart from an empty area.

---

## BUG-API-003 – `format` error is plain text, all other 400 errors are JSON

| Field | Value |
|---|---|
| **Endpoint** | `GET /search` |
| **Severity** | Low |
| **Test** | `test_search.py::test_search_invalid_format_error_is_json` |

**Steps**
1. `GET /search?q=Bangalore&format=xyz`
2. `GET /search?q=Bangalore&format=json&limit=abc`, for comparison

**Expected result**
Both errors use the same JSON shape: `{"error": {"code": 400, "message": "..."}}`

**Actual result**
1. `Content-Type: text/plain`, body `ERROR 400: Parameter 'format' must be one of: xml, geojson, geocodejson, json, jsonv2`
2. `Content-Type: application/json`, `{"error": {"code": 400, "message": "Parameter 'limit' must be a number."}}`

**Impact**
Clients that parse every error as JSON crash on this one.
