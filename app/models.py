"""app models"""

import random

QUESTIONS = {}
ANSWERS = {}

class Question:
    question_id = 1

    def __init__(self, title, question):
        """class constructor"""

        self.id = len(QUESTIONS) +1
        self.title = title
        self.question = question
        self.answers_id = random.randint(1, 100)

    def add(self):
        """method to add new question to questions"""

        QUESTIONS[self.id] = {"title": self.title,
                              "question": self.question,
                              "answers_id" : self.answers_id
                             }
        ANSWERS[self.answers_id] = {}

    @staticmethod
    def get_all():
        """method to fetch all questions"""

        return QUESTIONS

    @staticmethod
    def get_one(question_id):
        """method to fetch a question"""
        for key in QUESTIONS:
            if key == question_id:
                return QUESTIONS[key]


    @staticmethod
    def delete(question_id):
        """method to delete a question"""

        for key in QUESTIONS:
            if key == question_id:
                QUESTIONS.pop(key, None)
                return "deleted"

class Answer:
    def __init__(self, question_id, answer):
        answers_id = QUESTIONS[question_id]["answers_id"]
        self.answer_id = len(ANSWERS[answers_id]) +1
        self.question_id = question_id
        self.answer = answer

    def save(self):
        """method to add new answer to answers"""
        answers_id = QUESTIONS[self.question_id]["answers_id"]

        ANSWERS[answers_id][self.answer_id] = self.answer


    @staticmethod
    def get_all_answers(question_id):
        """method to fetch all answers to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        return ANSWERS[answers_id]

    @staticmethod
    def get_one(question_id, answer_id):
        """method to fetch an answer to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        return {"answer" : ANSWERS[answers_id][answer_id]}

    @staticmethod
    def delete_answer(question_id, answer_id):
        """method to delete an answer to a question"""

        answers_id = QUESTIONS[question_id]["answers_id"]

        ANSWERS[answers_id].pop(answer_id)
