from flask import render_template
from flask.ext.login import current_user
from showtime import app
from showtime.models import Episode

@app.route('/')
@app.route('/index')
def index():
    episodes = Episode.recent().all()
    return render_template('index.html', episodes = episodes, user = current_user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html'), 403

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 500