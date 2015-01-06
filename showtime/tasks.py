from showtime import app,db,manager
from sqlalchemy.exc import IntegrityError
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)

@manager.command
def update():
    "Download and update show episodes"
    from showtime.models import Episode,Show

    for show in Show.query.all():
        print('working on '+show.name)
        created,updated = show.update_episodes()

        for e in created:
            print("created S%2dE%2d - %s" %(e.season,e.episode,e.name))

        for e in updated:
            print("updated S%2dE%2d - %s" %(e.season,e.episode,e.name))

        print('finished %s : %d episodes created and %d changed '%(show.name,len(created),len(updated)))
