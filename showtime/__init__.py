from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.script import Manager
from flask_debugtoolbar import DebugToolbarExtension
from os import getcwd

app = Flask(__name__)
try:
    app.config.from_envvar('SHOWTIME_SETTINGS')
except RuntimeError:
    app.config.from_object('config')

db = SQLAlchemy(app)
from showtime.admin_views import admin

login_manager = LoginManager(app)

manager = Manager(app)

toolbar = DebugToolbarExtension(app)

from showtime import models,admin_views,views,auth,tasks
