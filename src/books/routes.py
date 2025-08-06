from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.books.models import Book
from src.core.dp_depends import get_db

router = APIRouter()

@router.get("/")
async def get_all_books(db: Annotated[Session, Depends(get_db)]):
    books = db.scalars(select(Book)).all()
    return books
