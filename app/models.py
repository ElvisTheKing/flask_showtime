from app import db

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128))
    slug = db.Column(db.String(64), index = True, unique = True)