import os

from sqlmodel import SQLModel, create_engine
from crud import create_records, select_records


def create_engine_with_db(db_name: str, echo: bool):
    sqlite_url = f"sqlite:///{db_name}"
    return create_engine(sqlite_url, echo=echo)


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)


def main():
    db_name = "garage.db"
    verbose = False
    delete_database = True
    if delete_database:
        try:
            os.remove(db_name)
        except FileNotFoundError:
            print(f"{db_name} not found")
            # exit()
    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)

    create_records(engine)
    select_records(engine)


if __name__ == "__main__":
    main()
