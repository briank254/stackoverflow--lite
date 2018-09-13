'''
Helper methods for models
'''
from ..dbconn import dbconn

def get_user_by_id(user_id):
    """
    return details for user with given id
    """
    conn = dbconn()
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM users WHERE user_id=%(user_id)s",
                {'user_id':user_id}
               )

    rows = cur.fetchone()

    cur.close()
    conn.close()

    return rows


def get_user_by_email(email):
    """
    returns user with given email
    """

    conn = dbconn()

    cur = conn.cursor()

    cur.execute('''SELECT * FROM users WHERE email=%(email)s''', 
    {'email':email})

    rows = cur.fetchone()

    cur.close()
    conn.close()

    return rows


def get_question_author(question_id):
    """
    returns question with specified id
    """
    conn = dbconn()
    cur = conn.cursor()

    cur.execute('''SELECT user_id FROM questions WHERE question_id=%(question_id)s''',
                {'question_id': question_id})

    rows = cur.fetchone()

    cur.close()
    conn.close()

    return rows

def get_user(email):
    """
    Method to check if user exists in database
    """
    conn = dbconn()

    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email=%(email)s", {'email':email})

    rows = cur.fetchone()

    cur.close()

    conn.close()

    return rows is not None

def get_password(email):
    """
    get users password
    """
    conn = dbconn()
    cur = conn.cursor()

    cur.execute('''SELECT password FROM users WHERE email=%(email)s''',
                {'email':email})

    rows = cur.fetchone()

    return rows

def check_respondent(email, question_id):
    """
    Check respondent against question author
    """
    user = get_user_by_email(email)[0]
    question_author = get_question_author(question_id)
    message = None
    code = None

    if question_author is None:
        message = {'error': 'Question not found'}
        code = 404

    elif user != question_author[0]:
        message = {'forbidden': 'You dont have permission to perform this operation'}
        code = 403

    return message, code

def get_question_details(question_id):
    """
    Get details of question with it's id
    """
    conn = dbconn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM questions WHERE question_id=%(question_id)s''',
                {'question_id':question_id})

    row = cur.fetchone()

    return row
