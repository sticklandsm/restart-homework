from typing import Optional

from fastapi import FastAPI, HTTPException

# One line of FastAPI imports here later &#x1f448;
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/heroes/")
def create_hero(hero: Hero):
  with Session(engine) as session:
    session.add(hero)
    session.commit()
  pass

@app.get("/heroes/{name}")
def get_hero(name: str):
    # implement part 2 here
    with Session(engine) as session:
      statement = select(Hero).where(Hero.name == name)
      hero = session.exec(statement).first() #returns list of all records that match
      if hero:
        return hero
      else:
        raise HTTPException(status_code=404, detail="Item not found")
    

@app.get("/heroes/")
def get_heroes():
    with Session(engine) as session:
      statement = select(Hero)
      heroes = session.exec(statement).all() #returns list of all records that match
      if heroes:
        return heroes
      else:
        raise HTTPException(status_code=404, detail="Item not found")
    pass
        
# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


# engine = create_engine("sqlite:///database.db")


# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     heroes = session.exec(statement).all() #returns list of all records that match
#     print(heroes)
#     print(type(heroes))
#     hero = session.exec(statement).first() #returns only first record
#     print(hero)