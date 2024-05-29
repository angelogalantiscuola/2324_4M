from sqlmodel import Session, select
from model import Garage, Cliente, Auto


def create_records(engine):
    with Session(engine) as session:

        garage = Garage(nome="Garage 1", posti_auto_disponibili=100)
        session.add(garage)
        session.commit()
        session.refresh(garage)
        print("Created garage:", garage)

        cliente = Cliente(nome="Mario", cognome="Rossi")
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        print("Created cliente:", cliente)

        auto = Auto(targa="AA123BB", modello="Fiat 500", cliente_id=cliente.id, garage_id=garage.id)
        session.add(auto)
        session.commit()
        session.refresh(auto)
        print("Created auto:", auto)


def select_records(engine):
    with Session(engine) as session:

        # select all garages
        garages = session.exec(select(Garage)).all()
        print("Garages:")
        for garage in garages:
            print(garage)
            # select all cars of the garage
            cars = session.exec(select(Auto).where(Auto.garage_id == garage.id)).all()
            print("Cars:")
            for car in cars:
                print(car)

        # select all clients
        clients = session.exec(select(Cliente)).all()
        print("Clients:")
        for client in clients:
            print(client)
            # select all cars of the client
            cars = session.exec(select(Auto).where(Auto.cliente_id == client.id)).all()
            print("Cars:")
            for car in cars:
                print(car)
