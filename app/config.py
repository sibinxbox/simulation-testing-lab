import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://appuser:apppassword@db:5432/appdb",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    APP_ENV = os.getenv("APP_ENV", "development")
