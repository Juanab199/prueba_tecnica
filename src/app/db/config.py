import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config.conf import load_env_vars

if os.getenv("DOCKER_ENV", False) == "true":
    DATABASE_URL = os.getenv("DATABASE_URL")
else:
    DATABASE_URL = load_env_vars().get("DATABASE_URL_RAIL")

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()