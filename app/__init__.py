from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from app.admin_views import admin

login_manager = LoginManager(app)


from app import models,admin_views,views,auth
