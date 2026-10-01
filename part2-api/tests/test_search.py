import pytest

import config
from utils.api_client import ApiClient
from utils.schemas import ErrorResponse, PlaceList


@pytest.mark.smoke
def test_search_city_returns_valid_places(api_client: ApiClient) -> None:
    response = api_client.search("Bangalore", limit=3)
    assert response.status_code == 200, response.text
    assert response.headers["content-type"].startswith("application/json")

    places = PlaceList.validate_python(response.json())
    assert 1 <= len(places) <= 3

    top = places[0]
    assert abs(top.lat - config.BANGALORE_LAT) < 0.2, top
    assert abs(top.lon - config.BANGALORE_LON) < 0.2, top


def test_search_with_address_details(api_client: ApiClient) -> None:
    response = api_client.search("Bangalore", limit=1, addressdetails=1)
    assert response.status_code == 200, response.text

    place = PlaceList.validate_python(response.json())[0]
    assert place.address is not None
    assert place.address.country_code == "in"
    assert place.address.state == "Karnataka"


def test_lookup_by_osm_id(api_client: ApiClient) -> None:
    response = api_client.lookup(config.BANGALORE_OSM_ID)
    assert response.status_code == 200, response.text

    places = PlaceList.validate_python(response.json())
    assert len(places) == 1
    assert places[0].osm_type == "relation"
    assert places[0].osm_id == int(config.BANGALORE_OSM_ID[1:])


def test_search_unknown_place_returns_empty_list(api_client: ApiClient) -> None:
    response = api_client.search("zzqxkjvbnmqwpl")
    assert response.status_code == 200, response.text
    assert response.json() == []


@pytest.mark.negative
def test_search_without_query_returns_400(api_client: ApiClient) -> None:
    response = api_client.search(None)
    assert response.status_code == 400

    body = ErrorResponse.model_validate(response.json())
    assert body.error.code == 400
    assert body.error.message == "Nothing to search for."


@pytest.mark.negative
def test_search_invalid_limit_returns_400(api_client: ApiClient) -> None:
    response = api_client.search("Bangalore", limit="abc")
    assert response.status_code == 400

    body = ErrorResponse.model_validate(response.json())
    assert body.error.message == "Parameter 'limit' must be a number."


@pytest.mark.negative
def test_search_invalid_format_returns_400(api_client: ApiClient) -> None:
    response = api_client.search("Bangalore", format="xyz")
    assert response.status_code == 400
    assert "Parameter 'format' must be one of" in response.text


@pytest.mark.negative
@pytest.mark.xfail(reason="BUG-API-001: empty q returns 200 [] instead of 400")
def test_search_empty_query_returns_400(api_client: ApiClient) -> None:
    response = api_client.search("")
    assert response.status_code == 400


@pytest.mark.negative
@pytest.mark.xfail(reason="BUG-API-003: format error is text/plain, other 400s are JSON")
def test_search_invalid_format_error_is_json(api_client: ApiClient) -> None:
    response = api_client.search("Bangalore", format="xyz")
    assert response.headers["content-type"].startswith("application/json")
