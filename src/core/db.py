from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pathlib import Path

engine = create_engine(f"sqlite:///../bookfor.db", echo=True)
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

