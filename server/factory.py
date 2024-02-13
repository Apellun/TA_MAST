from flask import Flask
from views.post_view import PostView
from views.get_view import GetView


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/get', view_func=GetView.as_view('get_view'))
    app.add_url_rule('/post', view_func=PostView.as_view('post_view'))
    return app