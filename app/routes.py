"""routes"""

import re
from flask import request, jsonify

from app.models import User
from . import app


@app.route('/api/v1/auth/signup', methods=['POST'])
def signup_user():

    """method to signup user"""

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if name is not None and name.strip() == "":
        return jsonify({"message": "Please fill in all the fields"}), 400

    email_regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    if not email_regex.match(email):
        return jsonify({"message": "Please enter a valid email"}), 400

    if password is not None and password.strip() == "":
        return jsonify({"message": "Please fill in all the fields"}), 400

    user = User(name=name, email=email, password=password)
    user.add()
    return jsonify({"message": "Account created successfully"}), 201


@app.route('/api/v1/auth/signin', methods=['POST'])
def login_user():

    """method to allow registered user to login"""

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email')
    password = request.json.get('password')

    email_regex = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    if not email_regex.match(email):
        return jsonify({"message": "Please enter a valid email"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    return jsonify({"message": "Login successful"}), 201
