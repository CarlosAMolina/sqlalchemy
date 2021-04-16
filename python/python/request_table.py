from sqlalchemy import text

import models
from database_connection import Database


def get_rows_using_the_model():
    s = models.students.select()
    with Database() as connection:
        result = connection.execute(s)
        for row in result:
            print(row)


def get_rows_using_sql_string():
    t = text("SELECT * FROM students")
    with Database() as connection:
        result = connection.execute(t)
        for row in result:
            print(row)


if __name__ == "__main__":
    get_rows_using_the_model()
    get_rows_using_sql_string()
