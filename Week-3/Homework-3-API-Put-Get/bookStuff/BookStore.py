from pydantic import BaseModel
from .BookItem import BookItem

class BookStore(BaseModel):
  name: str
  book_shelves: list[BookItem]
  pass