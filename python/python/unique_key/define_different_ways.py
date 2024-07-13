from typing import List

from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import declarative_base


foo_metadata = MetaData(schema="foo")
FooBase = declarative_base(metadata=foo_metadata)

class InTableArgs(FooBase):
    __tablename__ = "t_in_table_args"

    column_a = Column(INTEGER, primary_key=True)
    column_b = Column(INTEGER)

    __table_args__ = (UniqueConstraint("column_b", name="model_num2_key"),)



class InColumn(FooBase):
    __tablename__ = "t_in_column"

    column_a = Column(primary_key=True)
    column_b = Column(INTEGER, unique=True)


def assert_unique_columns_are_detected_correctly():
    assert InTableArgs.column_b.unique is None
    assert is_column_unique_in_table_args(InTableArgs, "column_b") is True
    assert InColumn.column_b.unique is True
    assert is_column_unique_in_table_args(InColumn, "column_b") is False

def is_column_unique_in_table_args(model, column_name):
    constraints = getattr(model, '__table_args__', [])
    for constraint in constraints:
        if isinstance(constraint, UniqueConstraint):
            if column_name in constraint.columns.keys():
                return True
    return False


if __name__ == "__main__":
    assert_unique_columns_are_detected_correctly()
