import pytest

from utils.api_client import ApiClient
from utils.schemas import StatusResponse


@pytest.mark.smoke
def test_status_endpoint_reports_ok(api_client: ApiClient) -> None:
    response = api_client.status()
    assert response.status_code == 200, response.text

    body = StatusResponse.model_validate(response.json())
    assert body.status == 0
    assert body.message == "OK"


@pytest.mark.negative
def test_request_without_user_agent_is_forbidden(api_client: ApiClient) -> None:
    # Nominatim has no API keys; access is controlled by the User-Agent policy instead
    response = api_client.get(
        "/search", {"q": "Bangalore", "format": "json"}, headers={"User-Agent": ""}
    )
    assert response.status_code == 403
    assert "Access denied" in response.text
