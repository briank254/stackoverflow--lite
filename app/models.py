"""app models"""

import uuid

QUESTIONS = {}
ANSWERS = {}


class Question:
    def __init__(self, question_id, title, question):
        """class constructor"""

        self.id = question_id
        self.title = title
        self.question = question
        self.answers_id = str(uuid.uuid4())

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
        try:
            if QUESTIONS[question_id]:
                return QUESTIONS[question_id]

        except (KeyError) as error:
            print(error)

    @staticmethod
    def delete(question_id):
        """method to delete a question"""

        try:
            if QUESTIONS[question_id]:
                QUESTIONS.pop(question_id, None)
                return "deleted"
        except (KeyError) as error:
            print(error)


class Answer:
    def __init__(self, answer_id, question_id, answer):

        self.answer_id = answer_id
        self.question_id = question_id
        self.answer = answer

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
