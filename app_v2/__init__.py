"""
API V2 initialisation as a module
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import CONFIG
from flasgger import Swagger
from database.tables import create_tables
from .auth import Signup, Signin, User
from .questions import QuestionsData, Question, UserQuestions
from .answers import AnswersData, Response
from .template import TEMPLATE


def create_app(config_name):
    """
    Application Factory
    """

    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    app.config.from_pyfile('config.py', silent=True)
    Swagger(app, template=TEMPLATE)
    api = Api(app)

    create_tables(app.config['DATABASE'])

    JWTManager(app)
    CORS(app)

    api.add_resource(Signup, '/api/v2/auth/signup')
    api.add_resource(Signin, '/api/v2/auth/signin')
    api.add_resource(User, '/api/v2/users')
    api.add_resource(QuestionsData, '/api/v2/questions')
    api.add_resource(Question, '/api/v2/questions/<int:question_id>')
    api.add_resource(UserQuestions, '/api/v2/user/questions')
    api.add_resource(AnswersData, '/api/v2/questions/<int:question_id>/answers')
    api.add_resource(Response, '/api/v2/questions/<int:question_id>/answers/<int:answers_id>')
    
    return app
