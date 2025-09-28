import os

DB_USER = os.getenv("POSTGRES_USER", "ims_user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "ims_pass")
DB_NAME = os.getenv("POSTGRES_DB", "ims_db")
DB_HOST = os.getenv("DB_HOST", "localhost")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
