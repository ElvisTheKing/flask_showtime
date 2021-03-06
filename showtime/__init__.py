from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.script import Manager
from flask_debugtoolbar import DebugToolbarExtension
from os import getcwd
from pytvdbapi import api as tvdb

app = Flask(__name__)
try:
    app.config.from_envvar('SHOWTIME_SETTINGS')
except RuntimeError:
    app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager(app)

manager = Manager(app)

toolbar = DebugToolbarExtension(app)

tvdb_api = lambda :tvdb.TVDB(app.config.get("TVDB_API_KEY"))

@app.after_request
def after_request(response):
    response.headers.add('X-Stage', 'Denial')
    return response

from showtime import models,admin_views,views,auth,tasks
