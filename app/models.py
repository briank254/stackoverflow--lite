"""app models"""

from datetime import datetime

USERS = []
QUESTIONS = []


class User:
    def __init__(self, name, email, password):
        """class constructor"""

        self.name = name
        self.email = email
        self.password = password

    def add(self):
        """method to add new user to users"""
        USERS.append(self)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }


class Question:
    question_id = 1

    def __init__(self, question=None):

        """class constructor"""

        self.question = question
        self.id = Question.question_id
        self.timestamp = "{}".format(
            datetime.utcnow().strftime("%d-%m-%Y %H:%M"))

        Question.question_id += 1

    def add(self):

        """method to add new user to users"""

        QUESTIONS.append(self)

    def get_all(self):

        """method to fetch all questions"""

        queries = [question.serialize()for question in QUESTIONS]

        return queries

    def serialize(self):
        return {
            "question": self.question,
            "id": self.id,
            "time": self.timestamp
        }

    def get_specific(self, question_id):
        """method to fetch a question"""

        for question in QUESTIONS:
            if question.id == question_id:
                return question

        return None

    def delete_specific(self, question_id):
        """method to delete a question"""

        for question in QUESTIONS:
            if question.id == question_id:
                QUESTIONS.remove(question)
                return question
        return False
