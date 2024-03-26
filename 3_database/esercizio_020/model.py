from sqlmodel import Field, Relationship, SQLModel

class Garage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    posti_auto_disponibili: int

    def visualizza_posti_auto_disponibili(self):
        return self.posti_auto_disponibili

    auto: list["Auto"] = Relationship(back_populates="garage")

class Cliente(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    cognome: str

    def visualizza_nome_cognome(self):
        return f"{self.nome} {self.cognome}"

    auto: list["Auto"] = Relationship(back_populates="cliente")

class Auto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    targa: str
    modello: str
    cliente_id: int | None = Field(default=None, foreign_key="cliente.id")
    garage_id: int | None = Field(default=None, foreign_key="garage.id")

    def visualizza_targa_modello(self):
        return f"{self.targa} {self.modello}"

    cliente: Cliente = Relationship(back_populates="auto")
    garage: Garage = Relationship(back_populates="auto")