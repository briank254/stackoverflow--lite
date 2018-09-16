"""
question model
Implements CRUD operations for questions
"""
from flask import abort
from flask_jwt_extended import get_jwt_identity
from ..dbconn import dbconn
from .helpers import (get_user_by_email, get_user_by_id, 
                      get_question_author, check_respondent, get_question_details)

class Questions:
    """
    questions object implementation
    """
    def __init__(self, title, question):
        self.title = title
        self.question = question
        

    def post_question(self):
        """
        create new question method
        """
        email = get_jwt_identity()
        user = get_user_by_email(email)

        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''select *
                       from questions where title=%(title)s''', {'title':self.title})

        rows = cur.fetchone()
        if rows:
           return {"Error": "A question with this title exists"}, 400

        #insert question to database
        cur.execute('''INSERT INTO questions
                        (user_id, 
                        title,
                        question
                         ) VALUES(%s, %s, %s)''',
                    [user[0], self.title, self.question])

        cur.close()
        conn.commit()
        conn.close()

        return {'message': 'question posted'}, 201

    @staticmethod
    def get_all_questions():
        """
        get al questions method
        """
        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''SELECT question_id, user_id, title, question from questions''')

        rows = cur.fetchall()

        questions = {}
        for row in rows:
            question = {
                'id':row[0],
                'author': get_user_by_id(row[1]),
                'title':row[2],
                'question': row[3]
                
            }
            questions.update(question)

        cur.close()
        conn.close()

        if questions == {}:
            return {'message': 'No questions available'}

        return questions

    @staticmethod
    def get_single_question(question_id):
        """
        get single question method
        """
        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''SELECT * from questions where question_id=%(question_id)s''', 
                    {'question_id':question_id})

        rows = cur.fetchone()
        if not rows:
            abort(404, 'question not found')

        question = {
            'id': rows[0],
            'author': get_user_by_id(rows[1]),
            'title': rows[2],
            'question': rows[3],
            
        }

        cur.close()
        conn.close()

        return {'question': question}

    @staticmethod
    def get_user_questions():
        """
        get users question
        """
        email = get_jwt_identity()

        user_id = get_user_by_email(email)[0]

        conn = dbconn()
        cur = conn.cursor()

        cur.execute('''select * from questions where user_id=%(user_id)s''', 
                    {'user_id': user_id})

        rows = cur.fetchall()

        questions = {}
        for row in rows:
            question = {
                'id':row[0],
                'title':row[2],
                'question': row[3],
                
            }
            questions.update(question)


        cur.close()
        conn.close()

        return questions

    @staticmethod
    def delete_question(question_id):
        """
        delete question method
        """
        email = get_jwt_identity()

        #only the question offer should be able to delete the question

        user = get_user_by_email(email)[0]
        question_author = get_question_author(question_id)

        if question_author is None:
            abort(404, 'question not found')
        if user != question_author[0]:
            abort(403, 'You dont have permission to perform this operation')

        conn = dbconn()
        cur = conn.cursor()
        cur.execute('''DELETE FROM questions WHERE question_id=%(question_id)s''',
                    {'question_id': question_id})

        cur.close()
        conn.commit()
        conn.close()


        return {'message':'question deleted'}, 200
    