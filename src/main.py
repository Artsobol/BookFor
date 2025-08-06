from fastapi import FastAPI
from src.books import book_router
import uvicorn

app = FastAPI()
app.include_router(book_router, prefix="/books", tags=["books"])

if __name__ == "__main__":


    uvicorn.run("src.main:app", port=8000, reload=True)