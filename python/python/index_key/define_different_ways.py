from typing import List

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Index
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import declarative_base


foo_metadata = MetaData(schema="foo")
FooBase = declarative_base(metadata=foo_metadata)

class InTableArgs(FooBase):
    __tablename__ = "t_in_table_args"

    column_a = Column(INTEGER, primary_key=True)
    column_b = Column(INTEGER)

    __table_args__ = (
        Index("column_a_index", "column_a"),
    )



class InColumn(FooBase):
    __tablename__ = "t_in_column"

    column_a = Column(primary_key=True, index=True, name="column_a_index")
    column_b = Column(INTEGER)


def assert_indexes_are_detected_correctly():
    assert get_indexes(InTableArgs) == ["column_a_index"]
    assert get_indexes(InColumn) == ['ix_foo_t_in_column_column_a_index']


def get_indexes(model) -> List[str]:
    table = inspect(model).mapped_table
    indexes = table.indexes
    return [index.name for index in indexes]

if __name__ == "__main__":
    assert_indexes_are_detected_correctly()

