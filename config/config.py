import os


class Config:
    BASE_URL = "https://insiderone.com"
    CAREERS_URL = "https://insiderone.com/careers/"
    TIMEOUT = 15
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    FILTER_LOCATION = "Istanbul"
    FILTER_TEAM = "Quality Assurance"
