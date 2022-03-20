from flask import Flask
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
