"""app models"""

import random

QUESTIONS = {}
ANSWERS = {}
QUESTION_COUNT = 0
ANSWER_COUNT = 0


class Question:
    def __init__(self, title, question):
        """class constructor"""
        global QUESTION_COUNT
        self.id = QUESTION_COUNT + 1
        self.title = title
        self.question = question
        self.answers_id = random.randint(1, 100)
        QUESTION_COUNT += 1

    def add(self):
        """method to add new question to questions"""

        QUESTIONS[self.id] = {"title": self.title,
                              "question": self.question,
                              "answers_id": self.answers_id
                             }
        ANSWERS[self.answers_id] = {}

    @staticmethod
    def get_all():
        """method to fetch all questions"""

        return QUESTIONS

    @staticmethod
    def get_one(question_id):
        """method to fetch a question"""

        return QUESTIONS[question_id]

    @staticmethod
    def delete(question_id):
        """method to delete a question"""

        for key in QUESTIONS:
            if key == question_id:
                return QUESTIONS.pop(key, None)


class Answer:
    def __init__(self, question_id, answer):
        global ANSWER_COUNT
        self.answer_id = ANSWER_COUNT + 1
        self.question_id = question_id
        self.answer = answer
        ANSWER_COUNT += 1

    def save(self):
        """method to add new answer to answers"""
        answers_id = QUESTIONS[self.question_id]["answers_id"]

        ANSWERS[answers_id][self.answer_id] = {"answer": self.answer}

    @staticmethod
    def get_all_answers(question_id):
        """method to fetch all answers to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        return ANSWERS[answers_id]

    @staticmethod
    def get_one(question_id, answer_id):
        """method to fetch an answer to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        return {"answer": ANSWERS[answers_id][answer_id]}

    @staticmethod
    def delete_answer(question_id, answer_id):
        """method to delete an answer to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        ANSWERS[answers_id].pop(answer_id)
