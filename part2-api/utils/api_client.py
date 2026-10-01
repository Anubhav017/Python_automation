import logging
import time
from typing import Any

import httpx

from config import API_BASE_URL, API_TIMEOUT, API_USER_AGENT, MIN_REQUEST_INTERVAL

log = logging.getLogger(__name__)


class ApiClientError(Exception):
    pass


class ApiClient:
    def __init__(
        self,
        base_url: str = API_BASE_URL,
        timeout: float = API_TIMEOUT,
        user_agent: str = API_USER_AGENT,
        token: str | None = None,
    ) -> None:
        headers = {"User-Agent": user_agent}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.client = httpx.Client(base_url=base_url, timeout=timeout, headers=headers)
        self._last_request = 0.0

    def _throttle(self) -> None:
        # the public server bans clients that go over 1 req/s, so space requests out
        wait = MIN_REQUEST_INTERVAL - (time.monotonic() - self._last_request)
        if wait > 0:
            time.sleep(wait)
        self._last_request = time.monotonic()

    def request(
        self, method: str, path: str, params: dict[str, Any] | None = None, **kwargs: Any
    ) -> httpx.Response:
        # None values are dropped so tests can leave a parameter out on purpose
        params = {k: v for k, v in (params or {}).items() if v is not None}
        self._throttle()
        try:
            response = self.client.request(method, path, params=params, **kwargs)
        except httpx.HTTPError as e:
            raise ApiClientError(f"{method} {path} failed: {e}") from e
        log.info("%s %s -> %s", method, response.url, response.status_code)
        return response

    def get(self, path: str, params: dict[str, Any] | None = None, **kwargs: Any) -> httpx.Response:
        return self.request("GET", path, params, **kwargs)

    def search(self, q: str | None, format: str = "json", **params: Any) -> httpx.Response:
        return self.get("/search", {"q": q, "format": format, **params})

    def reverse(self, lat: Any, lon: Any, format: str = "json", **params: Any) -> httpx.Response:
        return self.get("/reverse", {"lat": lat, "lon": lon, "format": format, **params})

    def lookup(self, osm_ids: str, format: str = "json", **params: Any) -> httpx.Response:
        return self.get("/lookup", {"osm_ids": osm_ids, "format": format, **params})

    def status(self) -> httpx.Response:
        return self.get("/status", {"format": "json"})

    def close(self) -> None:
        self.client.close()
