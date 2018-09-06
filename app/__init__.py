"""initializes app as a module"""

from flask import Flask
from . import routes

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
