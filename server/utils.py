from sqlite3 import Row
from typing import List


def validate_data(data):
    expected_fields = ["created_datetime", "content", "push_num"]
    for field in expected_fields:
        if not data.get(field):
            raise Exception(f"Поле {field} не может быть пустым.")
    if not isinstance(data.get("push_num"), int):
        raise Exception("Неправильный формат: push_num должно быть целым числом")
    
    
def rows_to_dict(rows: List[Row]):
    data = []
    for row in rows:
        data.append({
            'created_datetime': row['created_datetime'],
            'content': row['content'],
            'push_num': row['push_num']
            })
    return data