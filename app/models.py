"""app models"""

from datetime import datetime

USERS = []
QUESTIONS = []
ANSWERS = []


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

        """method to add new question to questions"""

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


class Answer:
    answer_id = 1

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.id = Answer.answer_id
        self.timestamp = "{}".format(
            datetime.utcnow().strftime("%d-%m-%Y %H:%M"))

        Answer.answer_id += 1

    def add(self):

        """method to add new answer to answers"""

        ANSWERS.append(self)

    def get_all_ans(self, question_id):

        """method to fetch all answers to a question"""

        responses = []
        for answer in ANSWERS:
            if answer.question.id == question_id:
                responses.append(answer.serialize())
        return responses

    def serialize(self):
        return {
            "answer": self.answer,
            "id": self.id,
            "time": self.timestamp,
            'question': self.question.serialize()

        }

    def get_one(self, que_id, ans_id):

        """method to fetch an answer to a question"""

        for answer in ANSWERS:
            if answer.id == ans_id and answer.question.id == que_id:
                return answer
        return None

    def delete_specific_answer(self, que_id, ans_id):

        """method to delete an answer to a question"""

        for answer in ANSWERS:
            if answer.id == ans_id and answer.question.id == que_id:
                ANSWERS.remove(answer)
                return answer
        return False
