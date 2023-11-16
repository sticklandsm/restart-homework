from pydantic import ValidationError
from bookStuff import Author,BookItem, BookStore
from typing import Union, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()



  
author1 = Author(name="John Jacob Hingleminer", author_id="SEAN-1999")
bookItem1 = BookItem(name="Moby Dick", author=author1, year_published=1955 )
my_book_items: Dict[str, BookItem] = {}

my_book_items["test1"] = bookItem1
my_book_items["test2"] = bookItem1



@app.put("/books/{name}")
def add_book(name: str, book_details: Union[BookItem, None] = None):
  my_book_items[name] = book_details
  
  return my_book_items
  pass


@app.get("/books/{name}")
def get_book(name: str):
  try:
    return my_book_items[name]
  except:
    raise HTTPException(status_code=404, detail="Item not found")
    
  
  pass


