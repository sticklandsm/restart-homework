from pydantic import ValidationError
from bookStuff import Author,BookItem, BookStore



def main():
  
  author1 = Author(name="John Jacob Hingleminer", author_id="SEAN-1999")
  bookItem1 = BookItem(name="Moby Dick", author=author1, year_published=1955 )
  bookItem2 = BookItem(name="Moby Dick 2: The Revenge", author=author1, year_published=2023 )
  bookStore1 = BookStore(name="Black Books", book_shelves=[bookItem1, bookItem2])
  
  print(bookStore1.__dict__)
  
  
  try:
    author1 = Author(name="John smooth", author_id="SEAN-1999")
  except ValidationError as e:
    print("Showing the author name validation for capitals: ", e)
  else:
    print(author1.__dict__)
    
  try:
    author2 = Author(name="John Smooth", author_id="SEAN19s")
  except ValidationError as e:
    print("Showing the author id validation. : ", e)
  else:
    print(author1.__dict__)
    
  try:
      bookItem1 = BookItem(name="Moby Dick", author=author1, year_published=2024 )
  except ValidationError as e:
    print("Showing the year_published validation: ", e)
  else:
    print(author1.__dict__)
    
  try:
    bookStore1 = BookStore(name="Black Books", book_shelves=[bookItem1, bookItem2, "Sean"])
  except ValidationError as e:
    print("Showing the book shelves have to full of books: ", e)
  else:
    print(author1.__dict__)
    
  print("WELL THAT'S ALL THE ERRORS. this is here to show that the code keeps flowing.")

if __name__ == "__main__":
  main()