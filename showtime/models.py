from showtime import db,tvdb_api
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date,datetime,timedelta
from flask.ext.login import UserMixin
from sqlalchemy.exc import IntegrityError

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), nullable = False)
    remote_id = db.Column(db.String(64), index = True, unique = True, nullable = False)
    episodes = db.relationship('Episode',backref = 'show')
    updated_at = db.Column(db.DateTime)

    @classmethod
    def updatable(cls):
        return cls.query.filter((cls.updated_at<=datetime.now()-timedelta(days=1))|(cls.updated_at == None))

    def update_episodes(self):
        api_show = tvdb_api().get_series(self.remote_id,'en')

        created = []
        updated = []
        for api_season in api_show:
            for api_episode in api_season:
                d = {
                    "season": api_season.season_number,
                    "episode": api_episode.EpisodeNumber,
                    "show_id": self.id,
                    "name": api_episode.EpisodeName,
                    "air_date": api_episode.FirstAired or None
                }

                episode = Episode(**d)

                try:
                    db.session.add(episode)
                    db.session.commit()
                    created.append(episode)
                except IntegrityError:
                    db.session.rollback()

                    episode = Episode.query.filter(
                        Episode.season == d['season'],
                        Episode.episode == d['episode'],
                        Episode.show_id == d['show_id']
                    ).first()

                    episode.name = d['name']
                    episode.air_date  = d['air_date']
                    if db.session.is_modified(episode):
                        db.session.commit()
                        updated.append(episode)

        self.updated_at = datetime.now()
        db.session.add(self)
        db.session.commit()

        return (created,updated)

    def __repr__(self):
        return "<%s>%s"%(self.__class__,self.name)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    season = db.Column(db.Integer, nullable = False)
    episode = db.Column(db.Integer, nullable = False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable = False)
    air_date = db.Column(db.Date)

    db.UniqueConstraint(show_id,season,episode)

    @classmethod
    def recent(cls):
        return cls.query.order_by(desc(cls.air_date)).limit(50)

    def is_in_future(self):
        return (self.air_date >= date.today())

    def search_string(self):
        return "%s S%02dE%02d" %(self.show.name,self.season,self.episode)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    remote_id = db.Column(db.String(256))
    email = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean())
    can_view_links = db.Column(db.Boolean())