from flask import render_template, redirect, request
import logging
from aereel import app
from database import Database


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    target_url  = request.form.get('url')
