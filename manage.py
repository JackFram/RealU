from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from project.sql import User
from project import app, db
import datetime

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        name="JackFram",
        email="erdos_zzh@163.com",
        password="admin",
        admin=True,
        confirmed=True,
        confirmed_on=datetime.datetime.now())
    )
    db.session.commit()


if __name__ == '__main__':
    manager.run()
