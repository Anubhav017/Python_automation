# Toptal E2E Framework - Anubhav Kumar

## Architecture
Python + Playwright (POM) + httpx + Pydantic + GitHub Actions

## Setup
```bash
copy .env.example .env      # optional, every value has a default
```
One `.env` at the repo root is read by both parts (`config.py` in each part loads it with python-dotenv). `.env` is git-ignored.

## Part 1 - UI E2E (https://automationteststore.com)

Covers login, search by three criteria (keyword, category, price), add to cart and checkout.

```bash
cd part1-e2e
pip install -r requirements.txt
playwright install chromium
pytest                 # 7 tests, HTML report -> part1-e2e/reports/report.html
pytest --headed        # watch the browser (or HEADLESS=false in .env)
```

```
part1-e2e/
  pytest.ini      report, trace/screenshot/video on failure
  config.py       reads .env: base url, headless, timeouts
  conftest.py     registers a fresh customer per session, saves login state
  pages/          page objects (locators + actions, no asserts)
  tests/          test_login, test_search, test_cart, test_checkout
  utils/          data_factory (UUID test data)
```

## Part 2 - API (OpenStreetMap: Nominatim + Notes API)

- **Nominatim** (read): search, reverse geocoding, lookup and status, plus negative cases and known bugs (as `xfail`).
- **Notes API on the OSM dev server** (write): create a note at a location, comment, close, reopen, delete, and the 401/403/404/409/400 errors. Needs `OSM_DEV_TOKEN`; without it the write tests are skipped. See [docs/API_TEST_CASES.md](docs/API_TEST_CASES.md#how-to-get-osm_dev_token) for how to get one.

```bash
cd part2-api
pip install -r requirements.txt
pytest                 # 30 tests, HTML report -> part2-api/reports/report.html
```

```
part2-api/
  pytest.ini      report, markers, xfail_strict
  config.py       reads .env: api urls, user agent, timeout, OSM dev token
  conftest.py     session-scoped api_client fixture
  utils/          api_client (httpx wrapper, 1 req/s throttle), notes_client, schemas (Pydantic)
  tests/          test_search, test_reverse, test_access, test_notes
```

## Docs
- Part 1 test flows and test cases: [docs/TEST_FLOWS.md](docs/TEST_FLOWS.md)
- Part 2 test cases: [docs/API_TEST_CASES.md](docs/API_TEST_CASES.md)
- Bug tickets (UI + API): [docs/BUG_REPORTS.md](docs/BUG_REPORTS.md)

## CI
[.gitlab-ci.yml](.gitlab-ci.yml) runs both parts as separate GitLab jobs on every push and merge request. Each job keeps its HTML report as a pipeline artifact and publishes JUnit results to the pipeline's **Tests** tab; Part 1 also keeps traces, screenshots and videos of failed tests. Set `OSM_DEV_TOKEN` under **Settings → CI/CD → Variables** to run the Notes write tests. The UI job retries failed tests twice, because the public demo store is shared and sometimes slow.

## Design Decisions
- **Playwright over Selenium:** Auto-wait, faster, trace on failure
- **Fresh account per run (UUID):** No shared demo credentials, safe for parallel and repeated runs
- **Page objects don't assert:** Tests own the checks, pages stay reusable
- **ApiClient wrapper:** One place for base URL, headers, throttling and logging; tests read like specs
- **httpx + Pydantic:** Schema validation, not just status code
- **Known bugs as strict xfail:** The report shows them, and a fix is noticed automatically
