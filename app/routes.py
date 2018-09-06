"""routes"""

import re
from flask import request, jsonify

from app.models import User, Question, Answer, QUESTIONS, ANSWERS
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


@app.route('/api/v1/questions/<int:id>/answers', methods=['POST'])
def post_answer(id):
    """method to allow user to post an answer to a question"""

    data = request.get_json()
    question = Question().get_specific(id)
    answer = data.get('answer')

    if not question:
        return jsonify({
            "message": "Question unavailable"}), 400

    if answer is not None and answer.strip() == "":
        return jsonify({
            "message": "Please post an answer"}), 400

    answer = Answer(question=question, answer=answer)
    answer.add()
    return jsonify({

        "message": "Your answer has been posted",
        "answer": answer.serialize()

    }), 201


@app.route('/api/v1/questions/<int:id>/answers', methods=['GET'])
def get_answers(id):
    """method to allow user to fetch answers to a question"""

    question = Question().get_specific(id)
    answer = []

    reply = Answer(question=question, answer=answer)
    answers = reply.get_all_ans(id)

    return jsonify({'answers': answers})


@app.route('/api/v1/questions/<int:que_id>/answers/<int:ans_id>', methods=['GET'])
def get_ans(que_id, ans_id):
    """method to allow user to fetch an answer to a question"""

    question = Question().get_specific(id)
    answer = []

    ans = Answer(question=question, answer=answer)
    answer = ans.get_one(que_id, ans_id)

    if not answer:
        return jsonify({
            "message": "Answer does not exist"}), 404

    return jsonify({'answer': answer.serialize()})


@app.route('/api/v1/questions/<int:que_id>/answers/<int:ans_id>', methods=['DELETE'])
def delete_ans(que_id, ans_id):
    """method to allow user to delete an answer to a question"""

    question = Question().get_specific(id)
    answer = []

    ans = Answer(question=question, answer=answer)
    answer = ans.delete_specific_answer(que_id, ans_id)

    if not answer:
        return jsonify({
            "message": "Answer does not exist"}), 404

    return jsonify({
        "message": "Delete Successful"}), 200


@app.route('/api/v1/questions/<int:que_id>/answers/<int:ans_id>', methods=['PUT'])
def update_answer(que_id, ans_id):
    """method to allow user to update an answer to a question"""

    data = request.get_json()
    ans = data.get('answer')
    question = Question().get_specific(id)

    answer = []
    answer = Answer(question=question, answer=answer).get_one(que_id, ans_id)

    if not answer:
        return jsonify({
            "message": "Answer does not exist"}), 404

    index = ANSWERS.index(answer)

    if answer:
        ANSWERS[index].answer = ans

    return jsonify({
        "message": "Answer updated successfully",
        "answer": answer.serialize()
    }), 200
