"""
Routes
"""
import re
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from jsonschema import validate, ValidationError
from database.models.user_model import Users
from .schemas import SIGNUP_SCHEMA

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")

class Signup(Resource):
    def post(self):
        data = request.json
        validate(data, SIGNUP_SCHEMA) 

        if not re.match(EMAIL_REGEX, data['email']):
            return{"message":"Invalid Email"}

        new_user = Users(data['first_name'],
                         data['last_name'],
                         data['email'],
                         data['password']
                        )
        response = new_user.signup()

        return response 


