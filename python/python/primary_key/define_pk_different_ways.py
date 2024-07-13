from typing import List

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import declarative_base


foo_metadata = MetaData(schema="foo")
FooBase = declarative_base(metadata=foo_metadata)

class PkInTableArgs(FooBase):
    __tablename__ = "t_pk_in_table_args"

    column_a = Column(INTEGER)
    column_b = Column(INTEGER)
    column_c = Column(INTEGER)

    __table_args__ = (
        PrimaryKeyConstraint("column_a", "column_b"),
    )


class PkInColumn(FooBase):
    __tablename__ = "t_pk_in_column"

    column_a = Column(INTEGER, primary_key=True)
    column_b = Column(INTEGER, primary_key=True)
    column_c = Column(INTEGER)


def get_pks(model) -> List[str]:
    """https://stackoverflow.com/a/10594091"""
    return [key.name for key in inspect(model).primary_key]


def assert_pks_are_detected_correctly():
    assert get_pks(PkInTableArgs) == ["column_a", "column_b"]
    assert get_pks(PkInColumn) == ["column_a", "column_b"]

if __name__ == "__main__":
    assert_pks_are_detected_correctly()

