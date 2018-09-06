"""routes"""

import re
from flask import request, jsonify

from app.models import User, Question, QUESTIONS
from . import app


@app.route('/api/v1/auth/signup', methods=['POST'])
def signup_user():

    """method to signup user"""

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if name is not None and name.strip() == "":
        return jsonify({"message": "Please fill in all the fields"}), 400

    email_regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    if not email_regex.match(email):
        return jsonify({"message": "Please enter a valid email"}), 400

    if password is not None and password.strip() == "":
        return jsonify({"message": "Please fill in all the fields"}), 400

    user = User(name=name, email=email, password=password)
    user.add()
    return jsonify({"message": "Account created successfully"}), 201


@app.route('/api/v1/auth/signin', methods=['POST'])
def login_user():

    """method to allow registered user to login"""

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email')
    password = request.json.get('password')

    email_regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    if not email_regex.match(email):
        return jsonify({"message": "Please enter a valid email"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    return jsonify({"message": "Login successful"}), 201

@app.route('/api/v1/questions/', methods=['POST'])
def post_question():

    """method to allow user to post a question"""

    data = request.get_json()
    question = data.get('question')

    if question is not None and question.strip() == "":
        return jsonify({
            "message": "Please post a question"}), 400

    question = Question(question=question)
    question.add()
    return jsonify({
        "message": "Your query has been posted"}), 201


@app.route('/api/v1/questions/', methods=['GET'])
def get_all_questions():

    """method to allow user to fetch all questions"""

    query = Question()
    questions = query.get_all()

    return jsonify({
        'questions': questions})


@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_specific_question(id):

    """method to allow user to fetch a specific question"""

    query = Question()
    question = query.get_specific(id)

    if not question:
        return jsonify({"message": "Query does not exist"}), 404

    return jsonify({
        'questions': question.serialize()})


@app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
def delete_specific_question(id):

    """method to allow user to delete a question"""

    query = Question()
    question = query.delete_specific(id)

    if not question:
        return jsonify({"message": "Query does not exist"}), 404

    return jsonify({

        "message": "Question deleted successfully"}), 200


@app.route('/api/v1/questions/<int:id>', methods=['PUT'])
def update_question(id):

    """method to allow user to update a question"""

    data = request.get_json()
    query = data.get('question')
    question = Question().get_specific(id)

    if not question:
        return jsonify({"message": "Query does not exist"}), 404

    index = QUESTIONS.index(question)

    if question:
        QUESTIONS[index].question = query

    return (jsonify({
        "message": "Question updated successfully"}), 201)
