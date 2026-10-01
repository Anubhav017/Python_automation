import os
from pathlib import Path

from dotenv import load_dotenv

# one .env at the repo root is shared by part1 and part2
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

API_BASE_URL = os.getenv("API_BASE_URL", "https://nominatim.openstreetmap.org").rstrip("/")
API_USER_AGENT = os.getenv("API_USER_AGENT", "Toptal-Test-Anubhav/1.0")
API_TIMEOUT = float(os.getenv("API_TIMEOUT", "20"))

# OpenStreetMap Notes API on the dev server, so test notes never reach the live map
OSM_API_URL = os.getenv("OSM_API_URL", "https://master.apis.dev.openstreetmap.org/api/0.6").rstrip("/")
# OAuth2 token (scope write_notes) of a dev server account; tests that write are skipped without it
OSM_DEV_TOKEN = os.getenv("OSM_DEV_TOKEN", "")
NOTE_TEXT = "Automated API test by Toptal-Test-Anubhav, safe to close"

# Nominatim usage policy: at most 1 request per second
MIN_REQUEST_INTERVAL = 1.0

# Bangalore city centre, used for search and reverse checks
BANGALORE_LAT = 12.9716
BANGALORE_LON = 77.5946
BANGALORE_OSM_ID = "R7902476"
