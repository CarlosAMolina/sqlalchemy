import models
from database_connection import Database


def _insert_rows():
    db = Database()
    rows_new = [
        models.Customers(
            name="Komal Pande", address="Koti, Hyderabad", email="komal@gmail.com"
        ),
        models.Customers(
            name="Rajender Nath", address="Sector 40, Gurgaon", email="nath@gmail.com"
        ),
        models.Customers(
            name="S.M.Krishna", address="Budhwar Peth, Pune", email="smk@gmail.com"
        ),
    ]
    db.session.add_all(rows_new)
    db.session.commit()


if __name__ == "__main__":
    _insert_rows()
