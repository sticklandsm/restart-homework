from pydantic import BaseModel, field_validator
from .Author import Author

class BookItem(BaseModel):
  name: str
  author: Author
  year_published: int
  
  @field_validator("year_published")
  @classmethod
  def check_year_published(cls, year_published):
    assert year_published > -3000 and year_published <= 2023, "The year is out of wack: " + str(year_published)
    return year_published
  pass