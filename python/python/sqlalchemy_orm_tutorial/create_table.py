from database_connection import Database
import models


def _create_tables():
    models.Base.metadata.create_all(Database().engine)


if __name__ == "__main__":
    _create_tables()
