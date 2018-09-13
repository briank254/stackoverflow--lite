"""initializes app as a module"""

from flask import Flask

APP = Flask(__name__, instance_relative_config=True)

from . import routes

APP.config.from_object('config')
