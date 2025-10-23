from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import get_settings
from sqlmodel import create_engine, SQLModel

settings = get_settings()

url_object = URL.create("postgresql",
                        username=settings.database_user,
                        password=settings.database_password,
                        host=settings.database_host,
                        database=settings.database_name)

print("Database URL:", url_object)

engine = create_engine(url_object)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    SQLModel.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
