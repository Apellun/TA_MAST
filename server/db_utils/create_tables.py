import sqlite3
from server.db_utils.commands import TABLE_INIT
from server.const import DATABASE_PATH


def create_tables():
    with sqlite3.connect(DATABASE_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(TABLE_INIT)
            connection.commit()
