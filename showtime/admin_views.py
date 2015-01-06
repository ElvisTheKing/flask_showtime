from showtime import db,models,app,tvdb_api
from flask import redirect,abort,url_for,jsonify
from flask.ext.admin import Admin,BaseView,expose,AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.form import rules
from flask.ext.login import current_user,login_required
from showtime.models import Episode,Show


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


class ShowView(AuthModelView):
    form_create_rules = (
        rules.Container('wrap', rules.Field('name')),
        'remote_id'
    )
    form_edit_rules = form_create_rules

    create_template = 'admin/show_create.html'

@app.route('/admin/show/autocomplete/<query>.json')
@login_required
def autocomplete(query):
    shows = tvdb_api.search(query,'en')
    items = map(lambda s: {"name": s.SeriesName, "id": s.seriesid, "info": s.Overview[0:150] if hasattr(s,'Overview') else ""},shows)

    return jsonify(items = list(items))


admin = Admin(app, name = "Showtime", index_view = AuthIndexView())
admin.add_view(ShowView(models.Show,db.session, name = "Shows"))
admin.add_view(AuthModelView(models.Episode,db.session, name = "Episodes"))
admin.add_view(AuthModelView(models.User,db.session, name = "Users"))