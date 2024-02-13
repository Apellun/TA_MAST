import sqlite3
from flask import request, Response
from flask.views import View
from const import DATABASE_PATH
from db_utils.commands import GET_ALL_ENTRIES
from utils import rows_to_dict


class GetView(View):
    methods = ['GET']

    def dispatch_request(self):       
        if request.method == 'GET':
            try:
                with sqlite3.connect(DATABASE_PATH) as connection:
                    connection.row_factory = sqlite3.Row 
                    cursor = connection.cursor()
                    cursor.execute(GET_ALL_ENTRIES)
                    rows = cursor.fetchall()
                
                return rows_to_dict(rows)
            
            except Exception as e:
                print(e)
                return Response("Ошибка сервера", status=500)