from flask import render_template, redirect

from skylines import app
from .model import User

@app.route('/')
def index():
    return redirect('/flights/latest')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/users/')
def user_list():
    return ', '.join([user.name for user in User.query()])
