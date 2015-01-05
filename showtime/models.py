from showtime import db
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date
from flask.ext.login import UserMixin

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    remote_id = db.Column(db.String(64), index = True, unique = True)
    episodes = db.relationship('Episode',backref = 'show')

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    season = db.Column(db.Integer, nullable = False)
    episode = db.Column(db.Integer, nullable = False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable = False)
    air_date = db.Column(db.Date)

    db.UniqueConstraint(show_id,season,episode)

    def recent():
        return Episode.query.order_by(desc(Episode.air_date)).limit(50)

    def is_in_future(self):
        return (self.air_date >= date.today())

    def search_string(self):
        return "%s S%02dE%02d" %(self.show.name,self.season,self.episode)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    remote_id = db.Column(db.String(256))
    email = db.Column(db.String(256))
    oauth_token = db.Column(db.String(256))
    oauth_secret = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean())