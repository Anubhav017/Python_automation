# Part 2 – API Test Cases

**API under test:** [Nominatim](https://nominatim.org/release-docs/latest/api/Overview/), the OpenStreetMap geocoding service.
**What it does:** it turns a place name into coordinates (search) and coordinates into an address (reverse).

## How the checks work
- Every response is checked for its **status code**. Its **shape** is also checked with Pydantic models in `utils/schemas.py`: required fields, their types, and valid ranges (latitude between -90 and 90, longitude between -180 and 180).
- All calls go through `utils/api_client.py`. It sends the User-Agent header that Nominatim requires and keeps to the public server's limit of **1 request per second**.
- Tests marked **xfail** show a known bug. The test states what the API *should* do. It fails today, and the report shows it as "expected fail" with the bug ID. If the API gets fixed, the test starts passing, and pytest flags that (`xfail_strict`), so the bug ticket can be closed.

| ID | Test (tests/…) | Request | Expected |
|---|---|---|---|
| API-01 | `test_search.py::test_search_city_returns_valid_places` | `GET /search?q=Bangalore&limit=3` | 200, JSON, 1–3 valid places. The first one is within 0.2° of Bangalore's centre |
| API-02 | `test_search.py::test_search_with_address_details` | `GET /search?q=Bangalore&addressdetails=1` | 200. Address has country code `in` and state `Karnataka` |
| API-03 | `test_search.py::test_lookup_by_osm_id` | `GET /lookup?osm_ids=R7902476` | 200, exactly one place, OSM relation 7902476 |
| API-04 | `test_search.py::test_search_unknown_place_returns_empty_list` | `GET /search?q=zzqxkjvbnmqwpl` | 200 with an empty list `[]` |
| API-05 | `test_search.py::test_search_without_query_returns_400` | `GET /search` (no `q`) | 400, `{"error": {"code": 400, "message": "Nothing to search for."}}` |
| API-06 | `test_search.py::test_search_invalid_limit_returns_400` | `GET /search?q=Bangalore&limit=abc` | 400, "Parameter 'limit' must be a number." |
| API-07 | `test_search.py::test_search_invalid_format_returns_400` | `GET /search?q=Bangalore&format=xyz` | 400, the message lists the allowed formats |
| API-08 | `test_search.py::test_search_empty_query_returns_400` | `GET /search?q=` | 400. **xfail: BUG-API-001** |
| API-09 | `test_search.py::test_search_invalid_format_error_is_json` | `GET /search?format=xyz` | Error body is JSON. **xfail: BUG-API-003** |
| API-10 | `test_reverse.py::test_reverse_geocode_known_coordinates` | `GET /reverse?lat=12.9716&lon=77.5946` | 200. The place is in Karnataka, India, within 0.05° of the point |
| API-11 | `test_reverse.py::test_reverse_open_ocean_returns_unable_to_geocode` | `GET /reverse?lat=0&lon=-160` | 200, `{"error": "Unable to geocode"}` (valid point with nothing there) |
| API-12 | `test_reverse.py::test_reverse_without_lon_returns_400` | `GET /reverse?lat=12.9716` | 400, "Parameter 'lon' missing." |
| API-13 | `test_reverse.py::test_reverse_out_of_range_latitude_returns_400` | `GET /reverse?lat=999&lon=77.59` | 400. **xfail: BUG-API-002** |
| API-14 | `test_access.py::test_status_endpoint_reports_ok` | `GET /status` | 200, `status: 0`, `message: "OK"` |
| API-15 | `test_access.py::test_request_without_user_agent_is_forbidden` | `GET /search` with an empty User-Agent | 403 "Access denied" |

> **Note on 401:** Nominatim has no API keys or logins, so it never returns 401. Access is controlled by the usage policy instead: requests without a User-Agent get **403 Forbidden** (API-15).

## Sending locations to the map: OpenStreetMap Notes API
Nominatim only reads data. To test **creating, changing and deleting** data, the suite also uses the [OSM Notes API](https://wiki.openstreetmap.org/wiki/API_v0.6#Map_Notes_API). A note is a pin with a message, dropped on the map at a latitude and longitude (for example "this café is missing"). All tests run on OSM's **dev server** (`master.apis.dev.openstreetmap.org`), so nothing reaches the real map.

- **Login:** writing needs an OAuth2 token (`OSM_DEV_TOKEN`, scope `write_notes`). Without it the write tests are **skipped**, not failed. The no-login checks (401, 404, 400) still run.
- **Independent tests:** each write test creates its own note and closes it afterwards, so tests can run in any order.

| ID | Test (tests/test_notes.py::…) | Request | Expected |
|---|---|---|---|
| NOTE-01 | `test_create_note_at_location` | `POST /notes.json?lat=12.9716&lon=77.5946&text=…` | 200. Note is `open` at exactly that point, first comment is the text sent |
| NOTE-02 | `test_created_note_can_be_read_back` | `GET /notes/{id}.json` (no login) | 200, same note and same coordinates |
| NOTE-03 | `test_comment_on_note` | `POST /notes/{id}/comment.json` | 200. Two comments, the last one is `commented` with the new text |
| NOTE-04 | `test_close_note` | `POST /notes/{id}/close.json` | 200. Status `closed`, `closed_at` is set |
| NOTE-05 | `test_reopen_closed_note` | `POST /notes/{id}/reopen.json` | 200. Status back to `open` |
| NOTE-06 | `test_close_already_closed_note_returns_409` | close the same note twice | **409 Conflict** |
| NOTE-07 | `test_delete_note_as_normal_user_returns_403` | `DELETE /notes/{id}.json` | **403 Forbidden**: only moderators may delete notes |
| NOTE-08 | `test_comment_on_unknown_note_returns_404` | `POST /notes/999999999/comment.json` | **404 Not Found** |
| NOTE-09 | `test_get_unknown_note_returns_404` | `GET /notes/999999999.json` | **404 Not Found** |
| NOTE-10 | `test_change_note_without_login_returns_401[comment, close, delete]` | comment, close or delete with no token | **401 Unauthorized**, "Couldn't authenticate you" |
| NOTE-11 | `test_create_note_with_invalid_input_returns_400[…]` | `lat=999` / `lat=abc` / no `text` | **400**, "The note is outside this world" / "lat was not a number" / "No text was given" |
| NOTE-12 | `test_change_note_with_invalid_token_returns_401[comment, close]` | comment or close with a made-up token | **401 Unauthorized**, "Couldn't authenticate you" (a bad token is not treated as a login) |

**Status codes covered across Part 2:** 200, 400, 401, 403, 404, 409.

### How to get `OSM_DEV_TOKEN`
1. Sign up at https://master.apis.dev.openstreetmap.org (separate from your normal OSM account) and confirm the email.
2. **My Settings → OAuth 2 applications → Register new application.** Redirect URI: `urn:ietf:wg:oauth:2.0:oob`. Permission: **Modify notes**. Save the Client ID and Client Secret.
3. Open in the browser, approve, and copy the code it shows:
   `https://master.apis.dev.openstreetmap.org/oauth2/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=write_notes`
4. Swap the code for a token:
   ```bash
   curl -X POST https://master.apis.dev.openstreetmap.org/oauth2/token \
     -d grant_type=authorization_code -d code=CODE \
     -d redirect_uri=urn:ietf:wg:oauth:2.0:oob \
     -d client_id=CLIENT_ID -d client_secret=CLIENT_SECRET
   ```
   The `access_token` in the reply is the value. Put it in `.env` locally, and add it in GitHub under **Settings → Secrets and variables → Actions** as the `OSM_DEV_TOKEN` repository secret.

## Run
```bash
cd part2-api
pip install -r requirements.txt
pytest                 # HTML report -> part2-api/reports/report.html
```
