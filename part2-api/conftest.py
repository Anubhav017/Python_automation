import pytest

import config
from utils.api_client import ApiClient
from utils.notes_client import NotesClient
from utils.schemas import Note


@pytest.fixture(scope="session")
def api_client():
    # one client for the whole run, so the 1 req/s throttle covers every test
    client = ApiClient()
    yield client
    client.close()


@pytest.fixture(scope="session")
def notes_client():
    """Notes API without a login, for read and 401 checks."""
    client = NotesClient()
    yield client
    client.close()


@pytest.fixture(scope="session")
def notes_auth_client():
    """Notes API logged in with the dev server token. Tests that need it skip when it is not set."""
    if not config.OSM_DEV_TOKEN:
        pytest.skip("OSM_DEV_TOKEN is not set, see README for how to get one")
    client = NotesClient(token=config.OSM_DEV_TOKEN)
    yield client
    client.close()


@pytest.fixture
def open_note(notes_auth_client: NotesClient):
    """A fresh open note for each test, so tests do not depend on each other's order."""
    response = notes_auth_client.create_note(config.BANGALORE_LAT, config.BANGALORE_LON, config.NOTE_TEXT)
    assert response.status_code == 200, response.text
    note = Note.model_validate(response.json())
    yield note
    # leave the dev map tidy: close whatever a test left open (already closed gives 409, that's fine)
    notes_auth_client.close_note(note.properties.id, "Automated test clean-up")
