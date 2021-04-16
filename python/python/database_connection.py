from sqlalchemy import create_engine


class Database:
    def __enter__(self):
        return self.engine.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def engine(self):
        return create_engine("sqlite:///college.db", echo=True)
