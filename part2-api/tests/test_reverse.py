import pytest

import config
from utils.api_client import ApiClient
from utils.schemas import ErrorResponse, GeocodeError, Place


@pytest.mark.smoke
def test_reverse_geocode_known_coordinates(api_client: ApiClient) -> None:
    response = api_client.reverse(config.BANGALORE_LAT, config.BANGALORE_LON, addressdetails=1)
    assert response.status_code == 200, response.text

    place = Place.model_validate(response.json())
    assert place.address is not None
    assert place.address.country_code == "in"
    assert place.address.state == "Karnataka"
    # the returned place is the nearest object, so it is close to the requested point
    assert abs(place.lat - config.BANGALORE_LAT) < 0.05
    assert abs(place.lon - config.BANGALORE_LON) < 0.05


def test_reverse_open_ocean_returns_unable_to_geocode(api_client: ApiClient) -> None:
    # valid coordinates in the middle of the Pacific, nothing to find there
    response = api_client.reverse(0, -160)
    assert response.status_code == 200, response.text

    body = GeocodeError.model_validate(response.json())
    assert body.error == "Unable to geocode"


@pytest.mark.negative
def test_reverse_without_lon_returns_400(api_client: ApiClient) -> None:
    response = api_client.reverse(config.BANGALORE_LAT, None)
    assert response.status_code == 400

    body = ErrorResponse.model_validate(response.json())
    assert body.error.message == "Parameter 'lon' missing."


@pytest.mark.negative
@pytest.mark.xfail(reason="BUG-API-002: lat outside -90..90 returns 200 'Unable to geocode' instead of 400")
def test_reverse_out_of_range_latitude_returns_400(api_client: ApiClient) -> None:
    response = api_client.reverse(999, config.BANGALORE_LON)
    assert response.status_code == 400
