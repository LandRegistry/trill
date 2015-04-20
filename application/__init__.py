from flask import Flask
from flask_bootstrap import Bootstrap

#doesn't seem to work with these lines in... Don't know why?
#from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

Bootstrap(app)
#db = SQLAlchemy(app)

app.config.from_object(os.environ.get('SETTINGS'))
