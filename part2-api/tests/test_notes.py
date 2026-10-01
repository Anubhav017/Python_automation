import pytest

import config
from utils.notes_client import NotesClient
from utils.schemas import Note

# notes are created on the OSM dev server; every write test needs OSM_DEV_TOKEN (see conftest)


@pytest.mark.smoke
def test_create_note_at_location(notes_auth_client: NotesClient) -> None:
    response = notes_auth_client.create_note(config.BANGALORE_LAT, config.BANGALORE_LON, config.NOTE_TEXT)
    assert response.status_code == 200, response.text

    note = Note.model_validate(response.json())
    assert note.properties.status == "open"
    assert abs(note.lat - config.BANGALORE_LAT) < 1e-6
    assert abs(note.lon - config.BANGALORE_LON) < 1e-6
    assert note.properties.comments[0].action == "opened"
    assert note.properties.comments[0].text == config.NOTE_TEXT

    notes_auth_client.close_note(note.properties.id, "Automated test clean-up")


def test_created_note_can_be_read_back(open_note: Note, notes_client: NotesClient) -> None:
    # read without a login: a note on the map is public
    response = notes_client.get_note(open_note.properties.id)
    assert response.status_code == 200, response.text

    note = Note.model_validate(response.json())
    assert note.properties.id == open_note.properties.id
    assert note.geometry.coordinates == open_note.geometry.coordinates


def test_comment_on_note(open_note: Note, notes_auth_client: NotesClient) -> None:
    response = notes_auth_client.comment(open_note.properties.id, "Confirmed, adding details")
    assert response.status_code == 200, response.text

    comments = Note.model_validate(response.json()).properties.comments
    assert len(comments) == 2
    assert comments[-1].action == "commented"
    assert comments[-1].text == "Confirmed, adding details"


def test_close_note(open_note: Note, notes_auth_client: NotesClient) -> None:
    response = notes_auth_client.close_note(open_note.properties.id, "Resolved")
    assert response.status_code == 200, response.text

    note = Note.model_validate(response.json())
    assert note.properties.status == "closed"
    assert note.properties.closed_at
    assert note.properties.comments[-1].action == "closed"


def test_reopen_closed_note(open_note: Note, notes_auth_client: NotesClient) -> None:
    notes_auth_client.close_note(open_note.properties.id)

    response = notes_auth_client.reopen_note(open_note.properties.id, "Still missing")
    assert response.status_code == 200, response.text

    note = Note.model_validate(response.json())
    assert note.properties.status == "open"
    assert note.properties.comments[-1].action == "reopened"


@pytest.mark.negative
def test_close_already_closed_note_returns_409(open_note: Note, notes_auth_client: NotesClient) -> None:
    notes_auth_client.close_note(open_note.properties.id)

    response = notes_auth_client.close_note(open_note.properties.id)
    assert response.status_code == 409, response.text


@pytest.mark.negative
def test_delete_note_as_normal_user_returns_403(open_note: Note, notes_auth_client: NotesClient) -> None:
    # only moderators may delete (hide) a note
    response = notes_auth_client.delete_note(open_note.properties.id, "Trying to delete")
    assert response.status_code == 403, response.text


@pytest.mark.negative
def test_comment_on_unknown_note_returns_404(notes_auth_client: NotesClient) -> None:
    response = notes_auth_client.comment(999999999, "Hello?")
    assert response.status_code == 404, response.text


# the checks below need no login, so they run even without OSM_DEV_TOKEN


@pytest.mark.negative
def test_get_unknown_note_returns_404(notes_client: NotesClient) -> None:
    response = notes_client.get_note(999999999)
    assert response.status_code == 404


@pytest.mark.negative
@pytest.mark.parametrize(
    "action",
    [
        lambda c: c.comment(1, "anonymous comment"),
        lambda c: c.close_note(1),
        lambda c: c.delete_note(1),
    ],
    ids=["comment", "close", "delete"],
)
def test_change_note_without_login_returns_401(notes_client: NotesClient, action) -> None:
    response = action(notes_client)
    assert response.status_code == 401
    assert "Couldn't authenticate you" in response.text


@pytest.mark.negative
@pytest.mark.parametrize(
    ("lat", "lon", "text", "message"),
    [
        (999, config.BANGALORE_LON, "bad latitude", "The note is outside this world"),
        ("abc", config.BANGALORE_LON, "latitude is not a number", "lat was not a number"),
        (config.BANGALORE_LAT, config.BANGALORE_LON, None, "No text was given"),
    ],
    ids=["lat-out-of-range", "lat-not-a-number", "no-text"],
)
def test_create_note_with_invalid_input_returns_400(
    notes_client: NotesClient, lat, lon, text, message
) -> None:
    # validation runs before anything is saved, so these never create a note
    response = notes_client.create_note(lat, lon, text)
    assert response.status_code == 400
    assert message in response.text
