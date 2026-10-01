import os
from pathlib import Path

from dotenv import load_dotenv

# one .env at the repo root is shared by part1 and part2
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

BASE_URL = os.getenv("BASE_URL", "https://automationteststore.com").rstrip("/")
HEADLESS = os.getenv("HEADLESS", "true").lower() != "false"

# the demo store is slow under shared traffic, so give expect() more room than the 5s default
EXPECT_TIMEOUT = int(os.getenv("EXPECT_TIMEOUT", "15000"))

SEARCH_KEYWORD = "shampoo"
CATEGORY = "Makeup"
