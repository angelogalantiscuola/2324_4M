import os
from database import create_db_and_tables, create_engine_with_db
from crud import (
    create_ClientAndHorse,
    delete_ClientAndHorse,
    select_ClientAndHorse,
    update_ClientAndHorse,
)


def main():
    db_name = "database_maneggio.db"
    verbose = False
    delete_database = True
    if delete_database:
        try:
            os.remove(db_name)
        except FileNotFoundError:
            print(f"{db_name} not found")

    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)
    create_ClientAndHorse(engine)
    select_ClientAndHorse(engine)
    update_ClientAndHorse(engine)
    delete_ClientAndHorse(engine)


if __name__ == "__main__":
    main()
  