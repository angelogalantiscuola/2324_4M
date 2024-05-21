from crud import create_records, select_records
from main import create_engine_with_db, create_db_and_tables
from sqlmodel import Session, select
from model import Garage, Cliente, Auto
import os
import tempfile
from sqlalchemy import create_engine

def test_create_engine_with_db():
    with tempfile.NamedTemporaryFile(suffix=".db") as temp_db:
        engine = create_engine_with_db(temp_db.name, echo=False)
        assert isinstance(engine, create_engine("sqlite://").__class__)
        assert engine.url.database.endswith(".db")

def test_create_db_and_tables():
    with tempfile.NamedTemporaryFile(suffix=".db") as temp_db:
        engine = create_engine_with_db(temp_db.name, echo=False)
        create_db_and_tables(engine)
        assert os.path.getsize(temp_db.name) > 0

def test_create_records():
    with tempfile.NamedTemporaryFile(suffix=".db") as temp_db:
        engine = create_engine_with_db(temp_db.name, echo=False)
        create_db_and_tables(engine)
        create_records(engine)
        with Session(engine) as session:
            assert session.get(Garage, 1) is not None
            assert session.get(Cliente, 1) is not None
            assert session.get(Auto, 1) is not None

def test_select_records():
    with tempfile.NamedTemporaryFile(suffix=".db") as temp_db:
        engine = create_engine_with_db(temp_db.name, echo=False)
        create_db_and_tables(engine)
        create_records(engine)
        select_records(engine)
        with Session(engine) as session:
            assert len(session.exec(select(Garage)).all()) == 1
            assert len(session.exec(select(Cliente)).all()) == 1
            assert len(session.exec(select(Auto)).all()) == 1

def test_Garage():
    garage = Garage(nome="Garage 1", posti_auto_disponibili=10)
    assert garage.nome == "Garage 1"
    assert garage.posti_auto_disponibili == 10
    assert garage.visualizza_posti_auto_disponibili() == 10

def test_Cliente():
    cliente = Cliente(nome="John", cognome="Doe")
    assert cliente.nome == "John"
    assert cliente.cognome == "Doe"
    assert cliente.visualizza_nome_cognome() == "John Doe"

def test_Auto():
    auto = Auto(targa="AB123CD", modello="Model X")
    assert auto.targa == "AB123CD"
    assert auto.modello == "Model X"
    assert auto.visualizza_targa_modello() == "AB123CD Model X"

def test_relationships():
    with tempfile.NamedTemporaryFile(suffix=".db") as temp_db:
        engine = create_engine_with_db(temp_db.name, echo=False)
        create_db_and_tables(engine)
        with Session(engine) as session:
            garage = Garage(nome="Garage 1", posti_auto_disponibili=10)
            cliente = Cliente(nome="John", cognome="Doe")
            auto = Auto(targa="AB123CD", modello="Model X", cliente=cliente, garage=garage)

            session.add(auto)
            session.commit()

            db_auto = session.get(Auto, auto.id)
            db_cliente = session.get(Cliente, cliente.id)
            db_garage = session.get(Garage, garage.id)

            assert db_auto.cliente_id == db_cliente.id
            assert db_auto.garage_id == db_garage.id
            assert db_auto in db_cliente.auto
            assert db_auto in db_garage.auto