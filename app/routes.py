"""routes"""

from flask import request, jsonify

from app.models import Question
from . import app

@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    """method to allow user to post a question"""

    data = request.get_json()
    title = data.get('title')
    question = data.get('question')

    if title is not None and title.strip() == "":
        return jsonify({
            "message": "Please fill in all fields"}), 400

    if question is not None and question.strip() == "":
        return jsonify({
            "message": "Please fill in all fields"}), 400

    new_question = Question(title, question)
    new_question.add()
    return jsonify({
        "message": "Your question has been posted"}), 201


@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    """method to allow user to fetch all questions"""

    response = Question.get_all()
    return jsonify({"questions": response})


@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_one_question(id):
    """method to allow user to fetch a specific question"""

    question = Question.get_one(id)

    if not question:
        return jsonify({"message": "Question does not exist"}), 404

    return jsonify({
        'questions': question})


@app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    """method to allow user to delete a question"""

    question = Question.delete(id)

    if not question:
        return jsonify({"message": "Question does not exist"}), 404

    return jsonify({

        "message": "Question deleted successfully"}), 200
