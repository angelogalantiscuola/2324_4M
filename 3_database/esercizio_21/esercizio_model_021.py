from sqlmodel import Field, Relationship, SQLModel
from typing import Optional

class link_cliente_album(SQLModel, table=True):
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id", primary_key=True)
    album_id: Optional[int] = Field(default=None, foreign_key="album.id", primary_key=True)

class Negozio(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    numeri_album: int

    def visualizza_album(self):
        return self.numeri_album

    album: list["Album"] = Relationship(back_populates="negozio")

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cognome: str

    def visualizza_nome_cognome(self):
        return f"{self.nome} {self.cognome}"

    album: list["Album"] = Relationship(back_populates="cliente")

class Album(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titolo: str
    artista: str
    codice_a_barre: str
    cliente_id: Optional[int] = Field(default=None, foreign_key="cliente.id")
    negozio_id: Optional[int] = Field(default=None, foreign_key="negozio.id")

    def visualizza_dettagli(self):
        return f"{self.titolo} {self.artista} {self.codice_a_barre}"

    cliente: Cliente = Relationship(back_populates="album")
    negozio: Negozio = Relationship(back_populates="album")