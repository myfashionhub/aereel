from flask import render_template, redirect, request
import logging

from application import create_session
from aereel import app
from users import Users


session = create_session()
users = Users(session)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = users.find_or_create('nessa_m00re@yahoo.com')
    return render_template('user.html', user=user)
