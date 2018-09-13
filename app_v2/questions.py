"""
Implements the questions endpoints
"""
from flask import request
from flask_restful import Resource
from jsonschema import validate, ValidationError
from flask_jwt_extended import jwt_required
from database.models.question_model import Questions
from .schemas import QUESTION_SCHEMA

class QuestionsData(Resource):
    """
    question operations
    """
    def get(self):
        """
        view all questions
        ---
        tags:
            - Questions
        description: View all questions
        responses:
            200:
                description: questions fetched
                schema:
                    $ref: '#/definitions/Question_details'
        """

        questions = Questions.get_all_questions()
            
        return ({"questions": questions})

    @jwt_required
    def post(self):
        """
        post a question
        ---
        tags:
            - Questions
        security:
            - Bearer: []
        description: Post question
        parameters:
            - name: Questions
              in: body
              schema:
                $ref: '#/definitions/Questions'
        responses:
            201:
                description: Question successfully created
            400:
                description: Bad request
        """
        data = request.json
        try:
            validate(data, QUESTION_SCHEMA)

            if not data['title'] and data['title'] .strip() == "":
                return ({
                "message": "Please fill in all fields"}), 400

            if data['question'] is not None and data['question'] .strip() == "":
                return ({
                    "message": "Please fill in all fields"}), 400

            new_question = Questions(data['title'], data['question'])

            result = new_question.post_question()

            return result
        
        except ValidationError as error:
            return {'message': str(error)}, 400

class Question(Resource):
    """
    single question operations
    """
    @jwt_required
    def get(self, question_id):
        '''
        get a single question
        ---
        tags:
            - Questions
        description: Fetch single question
        security:
            - Bearer: []
        parameters:
            - name: question_id
              in: path
              type: int
              description: Id of question to fetch
        responses:
            200:
                description: question fetched
                schema:
                    $ref: '#/definitions/Question_details'
            404:
                description: question not found
        '''

        response = Questions.get_single_question(question_id)

        return response
        

    @jwt_required
    def delete(self, question_id):
        """
        delete question
        ---
        tags:
            - Questions
        security:
            - Bearer: []
        description: Delete question
        parameters:
            - name: question_id
              in: path
              type: int
              description: Id of question to delete
        responses:
            200:
                description: question deleted
            404:
                description: question not found
        """
        response = Questions.delete_question(question_id)

        return response

class UserQuestions(Resource):
    """
    Specific User questions
    """
    @jwt_required
    def get(self):
        """
        Get specific user questions
        ---
        tags:
            - Questions
        """

        response = Questions.get_user_questions()

        return response