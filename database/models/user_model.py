"""
User model
Signup and Signin functionality
"""
import datetime
from flask import abort, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token, get_jwt_identity)
from .helpers import get_user, get_password, get_user_by_email
from ..dbconn import dbconn

class Users:
    """
    user class definition
    """
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = password

    def signup(self):
        """
        user signup method
        """

        data = [self.first_name, self.last_name, self.email, self.password_hash]
        print("<>", data)

        if get_user(self.email):
            return {'message': 'user already exists'}, 400

        conn = dbconn()
        cur = conn.cursor()

        sql = """INSERT INTO users (first_name, last_name, email, password)
                    VALUES(%s, %s, %s, %s)"""


        cur.execute(sql, data)

        cur.close()

        conn.commit()

        conn.close()

        return {'message': 'Account created'}, 201

    @staticmethod
    def signin(email, password):
        """
        signin method
        """
        if not get_user(email):
            return {'message': 'Invalid email or password'}, 404

        stored_password = get_password(email)[0]

        if not check_password_hash(stored_password, password):
            return {'message': 'Invalid email or password'}, 400

        expires = datetime.timedelta(days=14)

        access_token = create_access_token(email, expires_delta=expires)

        return {"success":"Signin successful",
                "access_token": access_token}

    @staticmethod
    def get_user_data():
        """
        get user details
        """
        email = get_jwt_identity()

        user = get_user_by_email(email)

        user_info = {}

        user_info['first_name']= user[1]
        user_info['last_name'] = user[2]
        user_info['email'] = user[3]
        
        return jsonify(user_info)

    @staticmethod
    def update_user(data):
        """
        Update user details
        """
        email = get_jwt_identity()

        user_id = get_user_by_email(email)[0]

        conn = dbconn()
        cur = conn.cursor()

        cur.execute('''UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s,
                       WHERE user_id=%(user_id)s''',
                    {'first_name': data.get('first_name'), 'last_name': data.get('last_name'),
                     'user_id': user_id})

        cur.close()
        conn.commit()
        conn.close()

        return {'message': 'Details updated successfully'}