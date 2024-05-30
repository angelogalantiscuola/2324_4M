from sqlmodel import Session, select
from model import Album, Cliente, Negozio, link_cliente_album
from termcolor import colored
def create_records(engine):
    with Session(engine) as session:
        negozio = Negozio(nome="Negozio 1", numeri_album=100)
        session.add(negozio)
        session.commit()
        session.refresh(negozio)
        print("Created negozio:", negozio)

        cliente = Cliente(nome="Mario", cognome="Rossi")
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        print("Created cliente:", cliente)

        album = Album(titolo="Album 1", artista="Artista 1", codice_a_barre="1234567890", cliente_id=cliente.id, negozio_id=negozio.id)
        session.add(album)
        session.commit()
        session.refresh(album)
        print("Created album:", album)


def select_records(engine):
    with Session(engine) as session:

        # select all negozi
        negozi = session.exec(select(Negozio)).all()
        print("Negozi:")
        for negozio in negozi:
            print(negozio)
            # select all albums of the negozio
            albums = session.exec(select(Album).where(Album.negozio_id == negozio.id)).all()
            print("Albums:")
            for album in albums:
                print(album)

        # select all clients
        clients = session.exec(select(Cliente)).all()
        print("Clients:")
        for client in clients:
            print(client)
            # select all albums of the client
            albums = session.exec(select(Album).where(Album.cliente_id == client.id)).all()
            print("Albums:")
            for album in albums:
                print(album)