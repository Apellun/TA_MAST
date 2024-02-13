import sqlite3
from datetime import datetime
from flask import request, Response
from flask.views import View
from const import DATABASE_PATH
from db_utils.commands import INSERT_ENTRY
from utils import validate_data
          
            
class PostView(View):
    methods = ['POST']
    def dispatch_request(self):
        if request.method == 'POST':
            data = request.json
            print(type(data))
            
            try:
                validate_data(data)
            except Exception as e:
                return Response(f"Некорректные данные.\n{e}", status=400)
            try:
                with sqlite3.connect(DATABASE_PATH) as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        INSERT_ENTRY,
                        (datetime.strptime(data.get("created_datetime"), '%Y%m%d %H:%M:%S'), data.get("content"), data.get("push_num"))
                    )
                    connection.commit()
                    return Response("OK", status=200)
                
            except sqlite3.IntegrityError as e:
                print(e)
                return Response(f"Некорректные данные. {e}", status=400)
            except Exception as e:
                print(e)
                return Response("Ошибка сервера", status=500)