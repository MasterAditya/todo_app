import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def reset_database():
    if os.path.exists("todo.db"):
        os.remove("todo.db")
    Base.metadata.create_all(bind=engine)

# Call reset_database to recreate the schema
reset_database()