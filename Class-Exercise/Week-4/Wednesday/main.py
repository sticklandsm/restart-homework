from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
  id: Optional[int] = Field (default=None, primary_key= True)
  name: str
  alter_ego: str
  age: Optional[int] = None
  
hero_1 = Hero(name="Deadpond", alter_ego="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", alter_ego="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", alter_ego="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    hero = session.exec(statement).all()
    print(hero)