from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.engine.base import Engine


def connect_postgresql(user: str, password: str, host: str, port: str, db: str) -> Engine:
    url = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(user, password, host, port, db)
    return create_engine(url, echo=True, future=True)

db = connect_postgresql("postgres", "admin", "localhost", "5432", "postgres")

meta = MetaData(db)
book_table = Table("books", meta, Column("title"), String)

app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class Book(BaseModel):
    name: str
    have_now: bool = False


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/api/v1/books")
async def read_books(book_id: int, q: Optional[str] = None):
    return {"book_id" : book_id, "q": q}
