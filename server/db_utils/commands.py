TABLE_INIT= """
    CREATE TABLE IF NOT EXISTS api_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_datetime DATETIME NOT NULL,
        content TEXT NOT NULL,
        push_num INTEGER NOT NULL
    );
"""
GET_ALL_ENTRIES = """
    SELECT * FROM api_table
"""
INSERT_ENTRY = """
    INSERT INTO api_table('created_datetime', 'content', 'push_num')
    VALUES(?, ?, ?)
"""