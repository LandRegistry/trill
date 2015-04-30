from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

from config import CONFIG_DICT

import os

app = Flask(__name__)

Bootstrap(app)
db = SQLAlchemy(app)

#app.config.from_object(os.environ.get('SETTINGS'))
app.config.update(CONFIG_DICT)
