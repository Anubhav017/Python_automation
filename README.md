# Playwright Framework

## Architecture
Python + Playwright (POM) + httpx + Pydantic + Locust + GitLab CI

## Setup
```bash
copy .env.example .env      # optional, every value has a default
```
One `.env` at the repo root is read by all parts (`config.py` in each part loads it with python-dotenv). `.env` is git-ignored.

## How to run (all 3 parts)
Run from the repo root. Each part has its own folder and `requirements.txt`.

| Part | Path | Run | Report |
|---|---|---|---|
| 1 - UI E2E | [part1-e2e/](part1-e2e/) | `pytest` | `part1-e2e/reports/report.html` |
| 2 - API | [part2-api/](part2-api/) | `pytest` | `part2-api/reports/report.html` |
| 3 - Load test | [part3-load/](part3-load/) | `python run_load_test.py` | `part3-load/reports/summary.md`, `locust_report.html` |

```bash
# Part 1 - UI E2E
cd part1-e2e
pip install -r requirements.txt
playwright install chromium
pytest
cd ..

# Part 2 - API
cd part2-api
pip install -r requirements.txt
pytest
cd ..

# Part 3 - Load test
cd part3-load
pip install -r requirements.txt
python run_load_test.py
cd ..
```

## How to check reports
Each run writes its report into the part's `reports/` folder. Open it from the repo root:

```bash
# Windows (PowerShell / cmd)
start part1-e2e\reports\report.html
start part2-api\reports\report.html
start part3-load\reports\locust_report.html
notepad part3-load\reports\summary.md

# macOS: use `open`, Linux: use `xdg-open`, e.g.
open part1-e2e/reports/report.html
```

| Part | Report | What it shows |
|---|---|---|
| 1 - UI E2E | `part1-e2e/reports/report.html` | pass/fail per test, with the error and log for failures |
| 1 - UI E2E | `part1-e2e/test-results/` | Playwright trace, screenshot and video of failed tests. Open a trace with `playwright show-trace part1-e2e/test-results/<test>/trace.zip` |
| 2 - API | `part2-api/reports/report.html` | pass/fail/xfail/skip per test, with a log line per request (method, URL, status) |
| 3 - Load | `part3-load/reports/summary.md` | response time before / during / after the load, and Locust totals |
| 3 - Load | `part3-load/reports/locust_report.html` | Locust charts: response time, requests/s, users over time |
| 3 - Load | `part3-load/reports/responses.txt` | full headers and timing of the analysed HTTP responses |

`reports/` is git-ignored, so run a part first to create its report. Saved copies from earlier runs are in [docs/evidence/](docs/evidence/).

In GitLab CI, open a pipeline, then a job, then **Browse** under *Job artifacts* to see the same files. Pass/fail results for Parts 1 and 2 are also on the pipeline's **Tests** tab.

## Part 1 - UI E2E (https://automationteststore.com)

Covers login, search by three criteria (keyword, category, price), add to cart and checkout, plus edge cases: login with empty fields, search with no results, and changing or removing cart items. Edge cases left out on purpose are listed in [docs/TEST_FLOWS.md](docs/TEST_FLOWS.md#not-automated-would-add-next).

```bash
cd part1-e2e
pip install -r requirements.txt
playwright install chromium
pytest                 # 11 tests, HTML report -> part1-e2e/reports/report.html
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
pytest                 # 32 tests, HTML report -> part2-api/reports/report.html
```

```
part2-api/
  pytest.ini      report, markers, xfail_strict
  config.py       reads .env: api urls, user agent, timeout, OSM dev token
  conftest.py     session-scoped api_client fixture
  utils/          api_client (httpx wrapper, 1 req/s throttle), notes_client, schemas (Pydantic)
  tests/          test_search, test_reverse, test_access, test_notes
```

## Part 3 - Load test (https://quickpizza.grafana.com)

Locust simulates 1000 users visiting the homepage over HTTPS within 15 s (66.67 new users/s, one visit each, a new TLS connection per user). A single-user probe measures response time before, during and after the load. QuickPizza is Grafana's public demo app made for load testing practice.

```bash
cd part3-load
pip install -r requirements.txt
python run_load_test.py   # ~1 min, reports -> part3-load/reports/ (summary.md, locust_report.html, responses.txt)
```

Locust only, with the web UI: `python -m locust -f locustfile.py`, then open http://localhost:8089.

```
part3-load/
  config.py          reads .env: target url, users, ramp time, probe settings
  locustfile.py      HomepageVisitor: one GET / per user, checks status and page title
  run_load_test.py   probe before -> Locust + probe during -> probe after, response capture, summary.md
```

Result: 1000/1000 visits passed, and response time did not change (probe median 805 ms before, 803 ms during). The full explanation, results, response-time targets and HTTP response analysis are in [docs/LOAD_TEST.md](docs/LOAD_TEST.md).

## Docs
- Part 1 test flows and test cases: [docs/TEST_FLOWS.md](docs/TEST_FLOWS.md)
- Part 2 test cases: [docs/API_TEST_CASES.md](docs/API_TEST_CASES.md)
- Bug tickets (UI and API): [docs/BUG_REPORTS.md](docs/BUG_REPORTS.md)
- Part 3 load test write-up and results: [docs/LOAD_TEST.md](docs/LOAD_TEST.md)

## CI
[.gitlab-ci.yml](.gitlab-ci.yml) runs Parts 1 and 2 as separate GitLab jobs on every push and merge request. The Part 3 `load` job is manual (start it from the pipeline page), because it sends 1000 requests to a public site. Each job keeps its HTML report as a pipeline artifact and publishes JUnit results to the pipeline's **Tests** tab; Part 1 also keeps traces, screenshots and videos of failed tests. Set `LOGIN_NAME`, `LOGIN_PASSWORD` and `LOGIN_FIRST_NAME` (masked) under **Settings → CI/CD → Variables** to run the login tests, and `OSM_DEV_TOKEN` to run the Notes write tests. The UI job retries failed tests twice, because the public demo store is shared and sometimes slow.

## Design Decisions
- **Playwright over Selenium:** Auto-wait, faster, trace on failure
- **Fixed account for login, fresh account for checkout:** Login credentials come from `.env` / CI variables so they can be parametrized and never sit in code; checkout registers a new UUID account per run so leftover cart items can't break it
- **Page objects don't assert:** Tests own the checks, pages stay reusable
- **ApiClient wrapper:** One place for base URL, headers, throttling and logging; tests read like specs
- **httpx + Pydantic:** Schema validation, not just status code
- **Known bugs as strict xfail:** The report shows them, and a fix is noticed automatically
- **Locust for load:** Python like the rest of the repo; a separate probe measures the user's view so load-generator overhead doesn't skew before/during numbers
