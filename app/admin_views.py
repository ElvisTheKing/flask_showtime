from app import admin,db,models
from flask.ext.admin.contrib.sqla import ModelView

admin.add_view(ModelView(models.Show,db.session, name = "Shows"))
admin.add_view(ModelView(models.Episode,db.session, name = "Episodes"))