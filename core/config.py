import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://kp-opt.ru")
    LOGIN = os.getenv("LOGIN")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10000))
