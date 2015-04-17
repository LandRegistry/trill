from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

Bootstrap(app)
db = SQLAlchemy(app)

app.config.from_object(os.environ.get('SETTINGS'))
