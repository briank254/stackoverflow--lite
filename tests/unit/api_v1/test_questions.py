import unittest
import json

from app import app


class TestQuestion(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def post_question(self):
        query_info = {
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions/',
                            data=json.dumps(query_info),
                            content_type='application/json'
                            )

        return res

    def test_post_question(self):
        res = self.post_question()
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):
        res = self.app.get('/api/v1/questions/')
        self.assertEqual(res.status_code, 200)

    def test_get_specific_question(self):
        """post question"""
        question = {
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions/',
                            data=json.dumps(question),
                            content_type='application/json'
                            )

        res = self.app.get('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)

    def test_update_question(self):
        question = {
            "question": "How do I refactor tests to pass?"
        }

        res = self.app.put('/api/v1/questions/1',
                           data=json.dumps(question),
                           content_type='application/json')

        self.assertEqual(res.status_code, 201)
    

    def test_delete_specific_question(self):
        """post question"""
        question = {
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions/',
                            data=json.dumps(question),
                            content_type='application/json'
                            )

        """delete question"""
        res = self.app.delete('/api/v1/questions/8')
        self.assertEqual(res.status_code, 200)

    
if __name__ == "__main__":
    unittest.main()
