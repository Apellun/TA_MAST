import requests
from requests.models import Response
from requests.exceptions import ConnectionError
from typing import List, Dict
from const import GET_URL, POST_URL


def check_satus_code(url: str, response: Response) -> None:
    if response.status_code == 404:
        raise Exception(f"Неверный адрес.\nCтраница {url} не найдена на сервере.")
    elif response.status_code == 405:
        raise Exception(f"Ошибка запроса.\nCтраница {url} не принимает запросы такого типа.")
    elif response.status_code == 400:
        raise Exception(f"Ошибка запроса.\n{response.text}")
    elif response.status_code == 500:
        raise Exception("Ошибка сервера.")
        
        
def send_data_request(content: str, push_num: int, datetime: str) -> None:
    data = {
            "content": content,
            "push_num": push_num,
            "created_datetime": datetime
            }
    try:
        response = requests.post(POST_URL, json=data)
        check_satus_code(POST_URL, response)
    except ConnectionError:
            raise Exception(f"Ошибка подключения к серверу.")
    
    
def get_data_request() -> List[Dict]:
    try:
        response = requests.get(GET_URL)
        check_satus_code(GET_URL, response)
        data = response.json()
        if not data:
            raise Exception(f"В базе пока нет записей или сервер вернул пустой список.")
        return data
    except ConnectionError:
        raise Exception(f"Ошибка подключения к серверу.")