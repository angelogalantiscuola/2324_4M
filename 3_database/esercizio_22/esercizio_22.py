import os
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

class PartecipanteShowLink(SQLModel, table=True):
    partecipante_id: int | None = Field(default=None, foreign_key="partecipante.id", primary_key=True)
    show_id: int | None = Field(default=None, foreign_key="show.id", primary_key=True)


class Show(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    location: str
    #numero_partecipanti: int

    partecipanti: list["Partecipante"] = Relationship(back_populates="shows", link_model=PartecipanteShowLink)
    giudici: list["Giudice"] = Relationship(back_populates="show")


class Partecipante(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    cognome: str

    def visualizza_nome_cognome(self):
        return f"{self.nome} {self.cognome}"

    shows: list[Show] = Relationship(back_populates="partecipanti", link_model=PartecipanteShowLink)


class Giudice(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    cognome: str
    eta: int

    show_id: int | None = Field(default=None, foreign_key="show.id")
    show: Show | None = Relationship(back_populates="giudici")

    def visualizza_nome_cognome(self):
        return f"{self.nome} {self.cognome}"
    

#create database
def create_engine_with_db(db_name: str, echo: bool):
    sqlite_url = f"sqlite:///{db_name}"
    return create_engine(sqlite_url, echo=echo)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)




def create_records(engine):
    with Session(engine) as session:

        show = Show(nome="Xfactor", location="Rimini")
        session.add(show)
        session.commit()
        session.refresh(show)
        print("Created show:", show)

        partecipante= Partecipante(nome="Mario", cognome="Rossi")
        session.add(partecipante)
        session.commit()
        session.refresh(partecipante)
        print("Created partecipante:", partecipante)

        # Create a PartecipanteShowLink instance to link the Partecipante and Show instances
        link = PartecipanteShowLink(partecipante_id=partecipante.id, show_id=show.id)
        session.add(link)
        session.commit()
        print("Created link:", link)

        giudice= Giudice(nome="Mario", cognome="Rossi", eta=30, show_id=show.id)
        session.add(giudice)
        session.commit()
        session.refresh(giudice)
        print("Created giudice:", giudice)



def select_records(engine):
    with Session(engine) as session:
        shows = session.exec(select(Show)).all()
        print("Show:")
        for show in shows:
            print(show)

        partecipanti = session.exec(select(Partecipante)).all()
        print("Partecipanti:")
        for partecipante in partecipanti:
            print(partecipante)

        giudici = session.exec(select(Giudice)).all()
        print("Giudici:")
        for giudice in giudici:
            print(giudice)
    

def main():
    db_name = "database.db"
    verbose = False
    delete_database = True
    if delete_database:
        try:
            os.remove(db_name)
        except FileNotFoundError:
            print(f"{db_name} not found")

    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)

    create_records(engine)
    select_records(engine)

if __name__ == "__main__":
    main()    

    

    
    

