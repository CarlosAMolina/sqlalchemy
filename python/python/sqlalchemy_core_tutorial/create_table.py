from database_connection import Database
import models

models.meta.create_all(Database().engine)
