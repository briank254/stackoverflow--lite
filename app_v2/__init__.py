"""
API V2 initialisation as a module
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from config import CONFIG
from database.tables import create_tables


def create_app(config_name):
    """
    Application Factory
    """

    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])

    create_tables(app.config['DATABASE'])

    JWTManager(app)

    return app
