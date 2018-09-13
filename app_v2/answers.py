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
        ---
        tags:
            - Answers
        security:
            - Bearer: []
        description: Get answers to a question
        parameters:
            - name: question_id
              in: path
              type: int
              description: Id of question you want to view questions
        responses:
            200:
                description: success
                schema:
                    $ref: '#/definitions/Answers'
            404:
                description: question not found
        """
        response = Answers.get_all_answers(question_id)

        return response

    @jwt_required
    def post(self, question_id):
        """
        post an answer to a question
        tags:
            - Answers
        security:
            - Bearer: []
        description: Post an answer to a question
        parameters:
            - name: question_id
              in: path
              type: int
              description: Id of question you want to answer
        responses:
            200:
                description: successfully posted
            400:
                description: bad request
            404:
                description: question not found
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
        """
        accept or reject answer to a question
        ---
        tags:
            - Answers
        security:
            - Bearer: []
        description: respond to answer
        parameters:
            - name: question_id
              in: path
              type: int
              description: Id of question
            - name: answer_id
              in: path
              type: int
              description: Id of answer you want to respond to
            - name: response
              in: body
              schema:
                $ref: '#/definitions/Response'
        responses:
            200:
                description: success
            400:
                description: Bad request
            403:
                description: Unauthorised, Only owners of question can mark answers
        """
        
        data = request.json
        
        validate(data, RESPONSE_SCHEMA)

        response = Answers.response_to_answer(question_id, answers_id, data)

        return response

        