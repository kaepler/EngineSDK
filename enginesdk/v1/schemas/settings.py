from os import getenv
from pydantic import BaseModel


class Settings(BaseModel):
    ENGINE_NAME: str = getenv("ENGINE_NAME", "Kaepler Engine")
    ENGINE_SLUG: str = getenv("ENGINE_SLUG", "kaepler-engine")
    VERSION: str = getenv("VERSION", "v1")
    REVISION: str = getenv("SHORT_SHA", "local")
    API_KEY_NAME: str = getenv("API_KEY_NAME", "access_token")
    COOKIE_DOMAIN: str = getenv("COOKIE_DOMAIN", "kaepler.com")
