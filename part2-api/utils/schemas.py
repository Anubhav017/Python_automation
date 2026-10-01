from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class Address(BaseModel):
    # address keys vary by place type (road, suburb, city, ...), keep the extras
    model_config = ConfigDict(extra="allow")

    country: str
    country_code: str = Field(min_length=2, max_length=2)
    state: str | None = None
    postcode: str | None = None


class Place(BaseModel):
    place_id: int
    licence: str
    osm_type: Literal["node", "way", "relation"]
    osm_id: int
    # the API sends coordinates as strings, pydantic converts them and checks the range
    lat: float = Field(ge=-90, le=90)
    lon: float = Field(ge=-180, le=180)
    display_name: str
    boundingbox: list[float] = Field(min_length=4, max_length=4)
    address: Address | None = None


PlaceList = TypeAdapter(list[Place])


class ErrorDetail(BaseModel):
    code: int
    message: str


class ErrorResponse(BaseModel):
    """Shape of 400 responses, e.g. {"error": {"code": 400, "message": "..."}}"""

    error: ErrorDetail


class GeocodeError(BaseModel):
    """Shape of a reverse lookup that found nothing: {"error": "Unable to geocode"}"""

    error: str


class StatusResponse(BaseModel):
    status: int
    message: str
    software_version: str
    data_updated: str


class NoteComment(BaseModel):
    model_config = ConfigDict(extra="allow")

    date: str
    action: Literal["opened", "commented", "closed", "reopened", "hidden"]
    text: str = ""
    # anonymous notes have no user
    user: str | None = None


class NoteProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int
    status: Literal["open", "closed", "hidden"]
    date_created: str
    closed_at: str | None = None
    comments: list[NoteComment]


class NoteGeometry(BaseModel):
    type: Literal["Point"]
    # GeoJSON order is [lon, lat]
    coordinates: list[float] = Field(min_length=2, max_length=2)


class Note(BaseModel):
    """A note as GeoJSON, e.g. GET /api/0.6/notes/{id}.json"""

    type: Literal["Feature"]
    geometry: NoteGeometry
    properties: NoteProperties

    @property
    def lon(self) -> float:
        return self.geometry.coordinates[0]

    @property
    def lat(self) -> float:
        return self.geometry.coordinates[1]
