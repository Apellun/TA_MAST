import os
from flask import Flask
from server.views.post_view import PostView
from server.views.get_view import GetView
from server.db_utils.create_tables import create_tables
from server.const import DATABASE_PATH


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/get', view_func=GetView.as_view('get_view'))
    app.add_url_rule('/post', view_func=PostView.as_view('post_view'))

    if not os.path.exists(DATABASE_PATH):
        create_tables()
        
    return app