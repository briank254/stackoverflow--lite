"""
Routes
"""
import re
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from jsonschema import validate, ValidationError
from database.models.user_model import Users
from .schemas import SIGNUP_SCHEMA, SIGNIN_SCHEMA

EMAIL_REGEX = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")


class Signup(Resource):
    def post(self):
        """
        Signup
        ---
        tags:
            - Auth
        description: Signup for an account
        parameters:
            - name: User
              in: body
              schema:
                $ref: '#/definitions/UserSignup'
        responses:
            201:
                description: Account created successfully
            400:
                description: Bad request
        """
        data = request.json
        try:
            validate(data, SIGNUP_SCHEMA) 

            if data['first_name'] is not None and data['first_name'].strip() == "":
                return ({"message" : "Please fill in all the fields"}), 400

            if data['last_name'] is not None and data['last_name'].strip() == "":
                return ({"message" : "Please fill in all the fields"}), 400

            if not re.match(EMAIL_REGEX, data['email']):
                return{"message":"Invalid Email"}, 400

            if data['password'] != data['confirm_password']:
                return {'message': 'Passwords do not match'}, 400

            new_user = Users(data['first_name'],
                                data['last_name'],
                                data['email'],
                                data['password']
                            )
            response = new_user.signup()

            return response 
        except ValidationError as error:
            return {'message': str(error)}, 400

class Signin(Resource):
    """
    Signin route handler
    """
    def post(self):
        """
        Signin
        ---
        tags:
            - Auth
        description: Sign into account
        parameters:
            - name: signin details
              in: body
              schema:
                $ref: '#/definitions/UserSignin'
        responses:
            200:
                description: signin successfull
            400:
                description: Bad request
            404:
                description: Wrong credentials
        """
       
        data = request.json
        try:
            validate(data, SIGNIN_SCHEMA)

            if not data['email']:
                return ({"msg": "Missing email parameter"}), 400
            if not data['password']:
                return ({"msg": "Missing password parameter"}), 400
        
            email = data['email']
            password = data['password']

            response = Users.signin(email, password)

            return response
        except ValidationError as error:
            return {'error': str(error)}, 400

class User(Resource):
    """
    User resource routes
    """
    @jwt_required
    def get(self):
        """
        Get user
        ---
        tags:
            - Users
        
        description: get user details
        responses:
            200:
                description: successful
        """
        
        return Users.get_user_data()

    @jwt_required
    def put(self):
        
        data = request.json
        
        return Users.update_user(data)

