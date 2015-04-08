from flask import Flask
import os

app = Flask(__name__)
from application import views
app.config.from_object(os.environ.get('SETTINGS'))
