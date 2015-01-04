from flask import render_template
from app import app
from app.models import Episode

@app.route('/')
@app.route('/index')
def index():
    episodes = Episode.recent().all()
    return render_template('index.html', episodes = episodes)