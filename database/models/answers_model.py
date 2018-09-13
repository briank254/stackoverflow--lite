"""
answer model
Implements Get answers, Make answers and Respond to answers
"""
from flask import abort
from flask_jwt_extended import get_jwt_identity
from ..dbconn import dbconn
from .helpers import (get_user_by_email, get_question_author, get_user_by_id,
                      check_respondent)

class Answers:
    """
    answer object implementation
    """
    def __init__(self, question_id, answer):
        self.question_id = question_id
        self.answer = answer

    def post_answer(self):
        """
        post answer method
        """
        email = get_jwt_identity()
        user = get_user_by_email(email)
        question = get_question_author(self.question_id)

        if question is None:
            abort(404, "question not found")

        conn = dbconn()
        cur = conn.cursor()
        
        cur.execute('''INSERT INTO answers (user_id, question_id, answer) VALUES (%s, %s, %s)''',
                    [user[0], self.question_id, self.answer])

        
        cur.close()
        conn.commit()
        conn.close()

        return {'message':'You have successfully answered the question'}, 200

    @staticmethod
    def get_all_answers(question_id):
        """
        get all answers method
        """

        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''select
                        answer_id, user_id, answer
                        from answers where question_id=%(question_id)s''',
                    {'question_id': question_id})

        rows = cur.fetchall()
        answers = []
        for row in rows:
            answer = {
                'id':row[0], 
                'user_name': get_user_by_id(row[1]),
                'answer' : row[2]
            }
            answers.append(answer)
        cur.close()
        conn.close()

        if answers == []:
            return {'message': 'no answers yet'}

        return answers


    @staticmethod
    def response_to_answer(question_id, answer_id, data):
        """
        reject or accept answer method
        """
        email = get_jwt_identity()
        user = get_user_by_email(email)[0]
        question_author = get_question_author(question_id)

        if not question_author:
            abort(404, 'question not found')
        if user != question_author[0]:
            abort(403, 'You dont have permission to perform this operation')

        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''select * from answers where answer_id=%(answer_id)s''',
                    {'answer_id': answer_id})

        row = cur.fetchone()

        if not row:
            abort(404, 'That answer does not exist')

        cur.execute('''UPDATE answers SET status =%(status)s 
                        WHERE answer_id =%(answer_id)s''',
                    {'answer_id': answer_id, 'status':data['status']})

        cur.close()
        conn.commit()
        conn.close()

        return {'message': 'answer has been updated'}
