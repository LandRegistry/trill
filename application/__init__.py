from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS'))
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://trill:@0.0.0.0:5432/trill"
db = SQLAlchemy(app)





from application import views, models
