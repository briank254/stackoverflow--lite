import unittest
import json
from app.id_gen import id_generator

from app import app


class TestQuestion(unittest.TestCase):
    """Test class for user ability to add,get,delete and update questions"""

    def setUp(self):
        """ Creates the app as a test client"""

        app.testing = True
        self.app = app.test_client()

        self.valid_question = {
            "title" : "tests",
            "question": "How do I refactor tests with database?"
        }

        self.invalid_question = {
            "title" : "",
            "question": "How do I refactor tests with database?"
        }

        self.valid_question2 = {
            "title" : "heroku",
            "question": "How do I refactor tests?"
        }

    def post_question(self, data):

        """post question helper"""


        response = self.app.post('/api/v1/questions',
                                 data=json.dumps(data),
                                 content_type='application/json'
                                )

        return response

    def test_post_valid_data_question(self):

        """method to test post question"""

        response = self.post_question(self.valid_question)
        self.assertEqual(response.status_code, 201)

    def test_post_invalid_data_question(self):

        """method to test post question"""

        response = self.post_question(self.invalid_question)

        self.assertEqual(response.status_code, 400)

    def test_post_duplicate_question(self):

        """method to test post question"""
        self.post_question(self.valid_question2)


        response = self.post_question(self.valid_question2)
        self.assertEqual(response.status_code, 400)

    def test_get_all_questions(self):

        """method to test get all questions"""

        res = self.app.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_get_one_question(self):

        """method to test getting a specific question"""
        question = {
            "title" : "Vim",
            "question": "How do I refactor tests with database?"
        }
        self.app.post('/api/v1/questions',
                      data=json.dumps(question),
                      content_type='application/json'
                     )

        question_id = id_generator("Vim")

        res = self.app.get('/api/v1/questions/'+str(question_id))
        self.assertEqual(res.status_code, 200)

    def test_non_existent_question(self):

        """method to test non-existent question"""

        res = self.app.get('/api/v1/questions/'+str(56))
        self.assertEqual(res.status_code, 404)


    def test_delete_question(self):

        """method to test deleting a specific question"""

        question = {
            "title" : "Blue",
            "question": "How do I refactor tests with database?"
        }

        self.app.post('/api/v1/questions',
                      data=json.dumps(question),
                      content_type='application/json'
                     )
        question_id = id_generator("Blue")
        res = self.app.delete('/api/v1/questions/'+str(question_id))
        self.assertEqual(res.status_code, 200)
