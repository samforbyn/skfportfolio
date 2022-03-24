from flask import Blueprint, render_template, request, url_for
from flask_mail import Mail, Message

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        print('email sent')
    else:
        return render_template('index.html')