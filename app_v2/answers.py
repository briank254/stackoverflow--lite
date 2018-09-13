"""
Implements the answers endpoints
"""
from flask import request
from flask_restful import Resource
from jsonschema import validate, ValidationError
from flask_jwt_extended import jwt_required
from database.models.answers_model import Answers
from .schemas import ANSWER_SCHEMA, RESPONSE_SCHEMA

class AnswersData(Resource):
    """
    question operations
    """
    def get(self, question_id):
        """
        get all answers to a question
        """
        response = Answers.get_all_answers(question_id)

        return response

    @jwt_required
    def post(self, question_id):
        """
        post an answer to a question
        """

        data = request.json
        validate(data, ANSWER_SCHEMA)

        if data['answer'] is not None and data['answer'].strip() == "":
            return ({
                "message": "Please provide an answer"}), 400


        new_answer = Answers(question_id, data['answer'])
        response = new_answer.post_answer()

        return response

class Response(Resource):
    '''
    User should be able to accept or reject an answer to a question
    '''
    @jwt_required
    def put(self, question_id, answers_id):
        
        data = request.json
        
        validate(data, RESPONSE_SCHEMA)

        response = Answers.response_to_answer(question_id, answers_id, data)

        return response

        