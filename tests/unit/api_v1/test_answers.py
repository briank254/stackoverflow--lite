import unittest
import json

from app import app


class TestAnswer(unittest.TestCase):
    """Test class for user ability to add,get,delete and update answers"""

    def setUp(self):
        """ Creates the app as a test client"""

        app.testing = True
        self.app = app.test_client()

    def post_answer(self):
        """
        post answer helper
        """
        question = {
            "question": "How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions/',
                            data=json.dumps(question),
                            content_type='application/json'
                           )

        answer = {
            "response": "You could first of all seperate your tests?"
        }

        res = self.app.post('/api/v1/questions/1/answers',
                            data=json.dumps(answer),
                            content_type='application/json'
                           )
        return res

    def test_post_answer(self):
        """
        method to test posting an answer
        """
        res = self.post_answer()
        self.assertEqual(res.status_code, 201)

    def test_get_answers(self):
        """
        method to test get all answers
        """
        res = self.app.get('/api/v1/questions/1/answers')
        self.assertEqual(res.status_code, 200)

    def test_update_answer(self):
        """
        method to test update of an answer
        """
        new_answer = {
            "answer": "it could be true"
        }

        response = self.post_answer()
        self.assertEqual(response.status_code, 201)

        answer_id = json.loads(response.data.decode())['answer']['id']

        edit_response = self.app.put('/api/v1/questions/1/answers/{}'
                                     .format(answer_id),
                                     data=json.dumps(new_answer),
                                     content_type='application/json')
        self.assertEqual(edit_response.status_code, 200)

    def test_delete_ans(self):
        """
        method to test deletion of an answer
        """
        response = self.post_answer()
        self.assertEqual(response.status_code, 201)

        delete_response = self.app.delete('/api/v1/questions/1/answers/1')
        self.assertEqual(delete_response.status_code, 200)

        result = self.app.get('/api/v1/questions/1/answers/1')
        self.assertEqual(result.status_code, 404)


if __name__ == "__main__":
    unittest.main()
