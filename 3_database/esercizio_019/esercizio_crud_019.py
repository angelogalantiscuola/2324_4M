from sqlmodel import Session, select
from models import Client, Horse


#CRUD
def create_ClientAndHorse(engine):
    with Session(engine) as session:
        client_1 = Client(name="Sante", surname="Tocco")
        client_2 = Client(name="Sokol", surname="Shkafi")
        session.add(client_1)
        session.add(client_2)
        session.commit()
        session.refresh(client_1)
        session.refresh(client_2)

        horse_1 = Horse(name="Bosi", age=34530, breed="Romanista")
        horse_2 = Horse(name="Spado", age=2007, breed="Rumeno")
        session.add(horse_1)
        session.add(horse_2)
        session.commit()
        session.refresh(horse_1)
        session.refresh(horse_2)
        
        client_1.horses.append(horse_1)
        client_1.horses.append(horse_2)
        client_2.horses.append(horse_1)
        client_2.horses.append(horse_2)
        session.commit()


def select_ClientAndHorse(engine):
    with Session(engine) as session:
        statement = select(Client, Horse).where(Client.id == Horse.id)
        results = session.exec(statement)
        for client, horse in results:
            print(client, horse)


def update_ClientAndHorse(engine):
    with Session(engine) as session:
        statement = select(Client, Horse).where(Client.id == Horse.id)
        results = session.exec(statement)
        for client, horse in results:
            client.name = "New name"
            horse.name = "New name"
        session.commit()


def delete_ClientAndHorse(engine):
    with Session(engine) as session:
        statement = select(Client, Horse).where(Client.id == Horse.id)
        results = session.exec(statement)
        for client, horse in results:
            session.delete(client)
            session.delete(horse)
        session.commit()


