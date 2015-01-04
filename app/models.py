from app import db

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    slug = db.Column(db.String(64), index = True, unique = True)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    season = db.Column(db.Integer)
    episode = db.Column(db.Integer)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))



