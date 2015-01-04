#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app,db
from sqlalchemy.exc import IntegrityError

app.debug=True
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

@manager.command
def update():
    "Download and update show episodes"
    from app.models import Episode,Show
    from pytvdbapi import api as tvdb_api
    api = tvdb_api.TVDB(app.config.get("TVDB_API_KEY"))

    for show in Show.query.all():
        print('working on '+show.name)
        api_show = api.get_series(show.remote_id,'en')

        created = 0
        updated = 0
        for api_season in api_show:
            for api_episode in api_season:
                d = {
                    "season": api_season.season_number,
                    "episode": api_episode.EpisodeNumber,
                    "show_id": show.id,
                    "name": api_episode.EpisodeName,
                    "air_date": api_episode.FirstAired
                }

                episode = Episode(**d)

                try:
                    db.session.add(episode)
                    db.session.commit()
                    created+=1
                    print("created S%2dE%2d - %s" %(d['season'],d['episode'],d['name']))

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
                        updated+=1
                        print("updated S%2dE%2d - %s" %(d['season'],d['episode'],d['name']))

        print('finished %s : %d episodes created and %d changed '%(show.name,created,updated))


if __name__ == '__main__':
    manager.run()