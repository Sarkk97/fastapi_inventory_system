import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///"+BASE_DIR+"/app.db"
    SECRET_KEY: str = "b3a1a4c92308e28718f220539b9b3366f85d1ce8126f8c8dc6c93b819ac78684"
    SIGNING_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()