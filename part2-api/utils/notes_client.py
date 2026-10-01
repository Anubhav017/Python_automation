from typing import Any

import httpx

from config import OSM_API_URL
from utils.api_client import ApiClient


class NotesClient(ApiClient):
    """OpenStreetMap Notes API: a note is a pin with a text, dropped on the map at lat/lon."""

    def __init__(self, token: str | None = None) -> None:
        super().__init__(base_url=OSM_API_URL, token=token)

    def create_note(self, lat: Any, lon: Any, text: str | None) -> httpx.Response:
        return self.request("POST", "/notes.json", {"lat": lat, "lon": lon, "text": text})

    def get_note(self, note_id: int) -> httpx.Response:
        return self.get(f"/notes/{note_id}.json")

    def comment(self, note_id: int, text: str | None) -> httpx.Response:
        return self.request("POST", f"/notes/{note_id}/comment.json", {"text": text})

    def close_note(self, note_id: int, text: str | None = None) -> httpx.Response:
        return self.request("POST", f"/notes/{note_id}/close.json", {"text": text})

    def reopen_note(self, note_id: int, text: str | None = None) -> httpx.Response:
        return self.request("POST", f"/notes/{note_id}/reopen.json", {"text": text})

    def delete_note(self, note_id: int, text: str | None = None) -> httpx.Response:
        # "delete" hides the note from the map; the API allows it for moderators only
        return self.request("DELETE", f"/notes/{note_id}.json", {"text": text})
