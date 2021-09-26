from fastapi import FastAPI
from sqlalchemy.orm import session
from core.config import settings
from db.session import engine
from db.base_class import Base


def create_tables():
    Base.metadata.create_all(bind=engine)
    '''Above code will connect our fastAPI with db engine'''

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    create_tables()
    return app

app = start_application()

@app.get("/")
def f1():
    return "Hello"


