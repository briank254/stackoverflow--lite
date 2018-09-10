import unittest
import json
from app.id_gen import id_generator
from app import app


class TestAnswer(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

        self.question = {
            "title": "Be you",
            "question": "How do I refactor tests with database?"
        }
        self.answer = {
            "answer": "You could first of all seperate your tests?"
        }
    def post_question(self, data):

        """post question helper"""

        response = self.app.post('/api/v1/questions',
                                 data=json.dumps(data),
                                 content_type='application/json'
                                )

        return response

    def post_answer(self, question_id, data):

        """post question helper"""

        res = self.app.post('/api/v1/questions/' +str(question_id) +'/answers',
                            data=json.dumps(data),
                            content_type='application/json'
                           )
        return res

    def test_post_answer(self):
        """method to test post answer to a question"""

        self.post_question(self.question)
        question_id = id_generator("Be you")

        res = self.post_answer(question_id, self.answer)
        self.assertEqual(res.status_code, 201)

    def test_get_all_answers(self):
        """method to test get all answers to a question"""
        question_id = id_generator("Be you")

        res = self.app.get('/api/v1/questions/' +str(question_id) +'/answers')
        self.assertEqual(res.status_code, 200)
