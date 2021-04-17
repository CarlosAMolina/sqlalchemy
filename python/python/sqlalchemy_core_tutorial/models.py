from sqlalchemy import MetaData, Table, Column, Integer, String

meta = MetaData()


students = Table(
    "students",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("lastname", String),
)
