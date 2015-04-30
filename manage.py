from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from application import app, db
from application.models import *

#app.config.from_object(os.environ.get('SETTINGS'))
from config import CONFIG_DICT

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
