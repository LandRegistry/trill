from flask import Flask
from flask_bootstrap import Bootstrap

import os

app = Flask(__name__)

Bootstrap(app)
from application import views
app.config.from_object(os.environ.get('SETTINGS'))
