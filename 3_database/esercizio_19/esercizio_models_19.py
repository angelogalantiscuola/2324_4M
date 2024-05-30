from sqlmodel import Field, Relationship, SQLModel
from typing import Optional


class Stables(SQLModel, table=True):
    client_id: Optional[int] = Field(default=None, foreign_key="client.id", primary_key=True)
    horse_id: Optional[int] = Field(default=None, foreign_key="horse.id", primary_key=True)


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    surname:  str = Field(index=True)
    horses: list["Horse"] = Relationship(back_populates="clients", link_model=Stables)


class Horse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: Optional[int] = Field(default=None, index=True)
    breed: str = Field(index=True)
    clients: list[Client] = Relationship(back_populates="horses", link_model=Stables)