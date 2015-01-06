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

tvdb_api = tvdb.TVDB(app.config.get("TVDB_API_KEY"))


from showtime import models,admin_views,views,auth,tasks
