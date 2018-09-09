"""routes"""

from flask import request, jsonify

from app.models import Question, Answer, QUESTIONS, ANSWERS
from . import app


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    """method to allow user to post a question"""

    data = request.get_json()
    title = data.get('title')
    question = data.get('question')

    if not title and title.strip() == "":
        return jsonify({
            "message": "Please fill in all fields"}), 400

    if question is not None and question.strip() == "":
        return jsonify({
            "message": "Please fill in all fields"}), 400

    for key, value in QUESTIONS.items():
        if value.get('question') == question:
            return jsonify({"message": "Question exists"}), 400

    new_question = Question(title, question)
    new_question.add()
    return jsonify({"message": "Your question has been posted"}), 201


@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    """method to allow user to fetch all questions"""
    questions = Question.get_all()
    if questions:
        for question_id in questions:
            question = questions[question_id]
            answers = ANSWERS[question["answers_id"]]
            question.update({"answers": answers})
        return jsonify({"questions": questions})

    return jsonify({"message": "No Questions"}), 404


@app.route('/api/v1/questions/<int:question_id>', methods=['GET'])
def get_one_question(question_id):
    """method to allow user to fetch a specific question"""

    try:
        question = Question.get_one(question_id)
        return jsonify({'questions': question})

    except KeyError:
        return jsonify({"message": "Question does not exist"}), 404


@app.route('/api/v1/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """method to allow user to delete a question"""

    question = Question.delete(question_id)

    if not question:
        return jsonify({"message": "Question does not exist"}), 404

    return jsonify({

        "message": "Question deleted successfully"}), 200


@app.route('/api/v1/questions/<int:question_id>/answers', methods=['POST'])
def post_answer(question_id):
    """method to allow user to post an answer to a question"""

    data = request.get_json()
    answer = data.get('answer')
    if answer is not None and answer.strip() == "":
        return jsonify({
            "message": "Please provide an answer"}), 400

    try:
        answers_id = Question.get_one(question_id)["answers_id"]
        answers = ANSWERS[answers_id]

        if answers:
            for answer_id in answers:
                ans = answers[answer_id]["answer"]
                if ans == answer:
                    return jsonify({"message": "Answer exists"}), 400

        answer = Answer(question_id, answer)
        answer.save()
        return jsonify({"message": "Your answer has been posted"}), 201

    except KeyError:
        return jsonify({
            "message": "Question does not exist"}), 404


@app.route('/api/v1/questions/<int:question_id>/answers', methods=['GET'])
def get_all_answers(question_id):
    """method to allow user to get all answers to a question"""

    try:
        question = Question.get_one(question_id)

        if question:
            answers = ANSWERS[question["answers_id"]]

            if answers:
                return jsonify({"answers": answers})

        return jsonify({"message": "Question does not have answers yet"}), 202

    except KeyError:
        return jsonify({"message": "Question does not exist"}), 404
