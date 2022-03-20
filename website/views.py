from flask import Blueprint, render_template, request, url_for

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template('homepage.html')