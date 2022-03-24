from flask import Flask
from flask_mail import Mail, Message
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY

    from .views import views

    mail = Mail(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'samforbyn@gmail.com'
    app.config['MAIL_PASSWORD'] = 'samforbyn@gmail.com'

    app.register_blueprint(views, url_prefix='/')

    return app
