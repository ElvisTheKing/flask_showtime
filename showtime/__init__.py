from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from showtime.admin_views import admin

login_manager = LoginManager(app)

manager = Manager(app)

from showtime import models,admin_views,views,auth,tasks
