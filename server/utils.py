from sqlite3 import Row
from typing import List
from datetime import datetime


def validate_data(data):
    expected_fields = ["created_datetime", "content", "push_num"]
    for field in expected_fields:
        if not data.get(field):
            raise Exception(f"Поле {field} не может быть пустым.")
    if not isinstance(data.get("push_num"), int):
        raise Exception("Неправильный формат: push_num должно быть целым числом")
    try:
        data["created_datetime"] = datetime.strptime(data["created_datetime"], '%Y%m%d %H:%M:%S')
    except:
        raise Exception("Неправильный формат даты.")
    return data

def rows_to_dict(rows: List[Row]):
    data = []
    for row in rows:
        data.append({
            'created_datetime': row['created_datetime'],
            'content': row['content'],
            'push_num': row['push_num']
            })
    return data