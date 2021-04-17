from sqlalchemy import and_

import models
from database_connection import Database


def _select_rows():
    result: list = Database().session.query(models.Customers).all()
    for row in result:
        _print_row(row)


def _select_row_by_primary_key():
    id_ = 2
    row = Database().session.query(models.Customers).get(id_)
    _print_row(row)


def _select_row_by_value():
    result = (
        Database()
        .session.query(models.Customers)
        .filter(and_(models.Customers.id > 2, models.Customers.name.like("%a%")))
    )
    print(f"Nomber of results {result.count()}")
    for row in result:
        _print_row(row)


def _select_first_row_in_db():
    _print_row(Database().session.query(models.Customers).first())


def _print_row(row):
    print(
        "Row ID: ",
        row.id,
        "Name: ",
        row.name,
        "Address:",
        row.address,
        "Email:",
        row.email,
    )


if __name__ == "__main__":
    _select_rows()
    _select_row_by_primary_key()
    _select_first_row_in_db()
    _select_row_by_value()
