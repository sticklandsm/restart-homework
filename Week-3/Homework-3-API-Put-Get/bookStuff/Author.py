from pydantic import BaseModel, field_validator

class Author(BaseModel):
  name: str
  author_id: str
  
  @field_validator("name")
  @classmethod
  def check_name_for_capitals(cls, name: str):
    
    split_name = name.split(" ")
    
    for word in split_name:
      assert word[0].isupper(), "Author name doesn't have capitals for the first letter of each name!: " + word
    return name
  
  @field_validator("author_id")
  @classmethod
  def check_author_id(cls, author_id: str):
    split_id = author_id.split("-")
    assert len(split_id) == 2, "Author id format error, there's too many or not enough hyphens"
    for part in split_id:
      assert len(part) == 4, "the parts of the Author_Id aren't the right length"
    assert split_id[1].isnumeric(), "There's no year in Author_Id: " + split_id[1]
    for letter in split_id[0]:
      assert letter.isupper(), "there's non capital letters in author_Id: " +  letter
    return author_id
  pass