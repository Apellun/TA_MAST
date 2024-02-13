import sqlite3
from flask import request, Response
from flask.views import View
from server.const import DATABASE_PATH
from server.db_utils.commands import INSERT_ENTRY
from server.utils import validate_data
          
            
class PostView(View):
    methods = ['POST']
    def dispatch_request(self):
        if request.method == 'POST':
            data = request.json
            
            try:
                validated_data = validate_data(data)
            except Exception as e:
                return Response(f"Некорректные данные.\n{e}", status=400)
            
            try:
                with sqlite3.connect(DATABASE_PATH) as connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        INSERT_ENTRY,
                        (validated_data.get("created_datetime"), validated_data.get("content"), validated_data.get("push_num"))
                    )
                    connection.commit()
                    return Response("OK", status=200)
            except Exception as e:
                print(e)
                return Response("Ошибка сервера", status=500)