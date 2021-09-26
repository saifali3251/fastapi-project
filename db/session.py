from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# if you don't want to install postgres or any database, use sqlite
# uncomment below lines if you would like to use sqlite and comment above one

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#   SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
# )


SessionLocal = sessionmaker(autocommit= False,autoflush=False,bind=engine)

# def get_db()-> Generator:
#   try:
#     db = SessionLocal()
#     yield db
#   finally:
#     db.close()


