import unittest
import json

from app import app


class TestQuestion(unittest.TestCase):
    """Test class for user ability to add,get,delete and update questions"""

    def setUp(self):
        """ Creates the app as a test client"""

        app.testing = True
        self.app = app.test_client()

    def post_question(self):

        """post question helper"""

        question = {
            "title" : "tests",
            "question": "How do I refactor tests with database?"
        }

        response = self.app.post('/api/v1/questions',
                                 data=json.dumps(question),
                                 content_type='application/json'
                                )

        return response

    def test_post_question(self):

        """method to test post question"""

        res = self.post_question()
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):

        """method to test get all questions"""

        res = self.app.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_get_one_question(self):

        """method to test getting a specific question"""

        question = {
            "title" : "tests",
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions',
                            data=json.dumps(question),
                            content_type='application/json'
                           )

        res = self.app.get('/api/v1/questions/2')
        self.assertEqual(res.status_code, 200)

    def test_delete_question(self):

        """method to test deleting a specific question"""

        question = {
            "title" : "tests",
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions',
                            data=json.dumps(question),
                            content_type='application/json'
                           )

        res = self.app.delete('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
