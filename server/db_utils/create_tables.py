import sqlite3
from server.utils.db_commands import TABLE_INIT
from server.utils.const import DATABASE_PATH


def init_db():
    with sqlite3.connect(DATABASE_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(TABLE_INIT)
            connection.commit()


if __name__ == "__main__":   
    init_db()