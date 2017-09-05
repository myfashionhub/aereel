import os

from flask import Flask
import flask_utils

from config import config


app = Flask(__name__, instance_relative_config=False)

env = os.environ['AEREEL_ENV']
app.config.update(**config[env])

from . import views
# from . import assets
