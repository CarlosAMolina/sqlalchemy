from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import declarative_base


foo_metadata = MetaData(schema="foo")
FooBase = declarative_base(metadata=foo_metadata)

class Foo(FooBase):
    __tablename__ = "t_foo"

    column_a = Column(INTEGER, primary_key=True)


class InTableArgs(FooBase):
    __tablename__ = "t_in_table_args"

    column_a = Column(INTEGER, primary_key=True)
    column_b = Column(INTEGER)
    column_c = Column(INTEGER)

    __table_args__ = (
        ForeignKeyConstraint(
            ["column_a"], ["t_foo.column_a"]
        ),
    )


class InColumn(FooBase):
    __tablename__ = "t_in_column"

    column_a = Column(ForeignKey("t_foo.column_a"), primary_key=True)
    column_b = Column(INTEGER)
    column_c = Column(INTEGER)


def assert_pks_are_detected_correctly():
    expected_result = ["t_foo.column_a"]
    assert get_fks(InTableArgs) == expected_result
    assert get_fks(InColumn) == expected_result


def get_fks(model) -> List[str]:
    """https://stackoverflow.com/a/61566835"""
    foreign_keys: set = model.__table__.foreign_keys
    foreign_keys: list = list(foreign_keys)
    return [foreign_key._colspec for foreign_key in foreign_keys]

if __name__ == "__main__":
    assert_pks_are_detected_correctly()

