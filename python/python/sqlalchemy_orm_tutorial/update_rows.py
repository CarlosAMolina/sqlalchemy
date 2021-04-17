import models
from database_connection import Database

# Changes are not commited to the db, you must use at the end:
# db.session.commit()


def _update_row_no_commit():
    db = Database()
    id_ = 2
    row = db.session.query(models.Customers).get(id_)
    _print_row(row)
    row.address = "NEW VALUE"
    _print_row(row)


def _update_rows_no_commit():
    db = Database()
    db.session.query(models.Customers).filter(models.Customers.id != 2).update(
        {models.Customers.name: f"Mr/Ms {models.Customers.name}"},
        synchronize_session=False,
    )
    result = db.session.query(models.Customers).all()
    for row in result:
        _print_row(row)


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


def _print_result_rows_count(result):
    print(f"Rows affected: {result.rowcount}")


if __name__ == "__main__":
    _update_row_no_commit()
    _update_rows_no_commit()
