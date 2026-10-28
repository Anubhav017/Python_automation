import os
from pathlib import Path

from dotenv import load_dotenv

# one .env at the repo root is shared by all parts
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# QuickPizza is Grafana's public demo app built for load testing practice
LOAD_BASE_URL = os.getenv("LOAD_BASE_URL", "https://quickpizza.grafana.com").rstrip("/")
# text every good homepage response must contain
LOAD_EXPECT_TEXT = os.getenv("LOAD_EXPECT_TEXT", "<title>QuickPizza</title>")
LOAD_USERS = int(os.getenv("LOAD_USERS", "1000"))
# all users arrive within this window, each one visits the homepage once
LOAD_RAMP_SECONDS = float(os.getenv("LOAD_RAMP_SECONDS", "15"))
# extra time after the ramp so the last visits can finish before Locust stops
LOAD_GRACE_SECONDS = int(os.getenv("LOAD_GRACE_SECONDS", "5"))

# single-user probe that measures response time before, during and after the load
PROBE_SAMPLES = int(os.getenv("PROBE_SAMPLES", "10"))
PROBE_INTERVAL = float(os.getenv("PROBE_INTERVAL", "0.5"))
REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "30"))
USER_AGENT = os.getenv("LOAD_USER_AGENT", "Python-Automation-Load/1.0")

REPORTS_DIR = Path(__file__).resolve().parent / "reports"
