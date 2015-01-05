from showtime import db,models,app
from flask import redirect,abort,url_for
from flask.ext.admin import Admin,BaseView,expose,AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

class AuthIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if (not current_user.is_anonymous()) and current_user.is_admin:
            return redirect('/admin/show/')
        else:
            abort(403)

class AuthModelView(ModelView):
    def is_accessible(self):
        return (not current_user.is_anonymous()) and current_user.is_admin

admin = Admin(app, name = "Showtime", index_view = AuthIndexView())
admin.add_view(AuthModelView(models.Show,db.session, name = "Shows"))
admin.add_view(AuthModelView(models.Episode,db.session, name = "Episodes"))
admin.add_view(AuthModelView(models.User,db.session, name = "Users"))