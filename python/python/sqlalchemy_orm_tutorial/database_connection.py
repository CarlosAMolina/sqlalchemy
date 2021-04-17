from sqlalchemy import create_engine


class Database:
    def __init__(
        self,
        db_dialect: str = "sqlite",
        db_name: str = "college.db",
    ):
        self._db_dialect = db_dialect
        self._db_name = db_name

    def __enter__(self):
        return self.engine.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def engine(self):
        return create_engine(f"{self._db_dialect}:///{self._db_name}", echo=True)
