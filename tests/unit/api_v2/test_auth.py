"""
tests for user authentication
"""
import json
import psycopg2
from flask import current_app

DATA = [{'first_name':'Gray', 'last_name': 'Hat',
         'email': 'gray@gmail.com', 'password':"password1234", "confirm_password":"password1234"},
        {'first_name':'Gray', 'last_name': 'Hat',
         'email': 'grayemail.com', 'password':"password1234", "confirm_password":"password1234"},
        {'first_name':'Gray', 'last_name': 'Hat',
         'email': ' ', 'password':"password1234"},
        {'first_name':'Gray', 'email': 'simo@mgugua.com','password':"password1234"},
        {'email':'gray@gmail.com', 'password':"password1234"},
        {'email': 'swwee@mail.com', 'password':"password1234"},
        {'email': 'gray@gmail.com', 'password': 'pass'},
        {'email': 'gray@gmail.com', 'password': ' '},
        {'email': 'gray@gmail.com'},
        {'first_name':'Gray', 'last_name': 'Hat',
         'email': 'grayhat@gmail.com', 'password':"password1234", "confirm_password":"password"}
       ]

def test_signup(test_client):
    """
    test that user accounts can be created
    """
    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[0]),
                                content_type='application/json')

    assert response.status_code == 201

def test_signup_mismatching_passwords(test_client):
    """
    test raises 400 error if passwords dont match
    """
    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[9]),
                                content_type='application/json')
    assert response.status_code == 400

def test_duplicate_signup(test_client):
    """
    test that an already signed in user cannot sign in again
    """

    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[0]),
                                content_type='application/json')

    assert response.status_code == 400

def test_signup_wrong_email_format(test_client):
    """
    test that a validation error is raised
    """
    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[1]),
                                content_type='application/json')
    assert response.status_code == 400

def test_signup_empty_string(test_client):
    """
    Should return 400
    """
    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[2]),
                                content_type='application/json')
    assert response.status_code == 400

def test_signup_missing_field(test_client):
    """
    test returns 400 error
    """
    response = test_client.post('/api/v2/auth/signup', data=json.dumps(DATA[3]),
                                content_type='application/json')
    assert response.status_code == 400

def test_signin(test_client):
    """
    test that user can signin into account
    """
    response = test_client.post('/api/v2/auth/signin', data=json.dumps(DATA[4]),
                                content_type='application/json')

    assert response.status_code == 200

    result = json.loads(response.data)

    assert "access_token" in result.keys()

def test_wrong_email(test_client):
    """
    test that it returns 404 error for wrong email
    """
    response = test_client.post('/api/v2/auth/signin', data=json.dumps(DATA[5]),
                                content_type='application/json')

    assert response.status_code == 404

def test_wrong_password(test_client):
    """
    test returns 400 error for wrong password
    """
    response = test_client.post('/api/v2/auth/signin', data=json.dumps(DATA[6]),
                                content_type='application/json')

    assert response.status_code == 400

def test_signin_empty_string(test_client):
    """
    test returns 400 for empty strings
    """
    response = test_client.post('/api/v2/auth/signin', data=json.dumps(DATA[7]),
                                content_type='application/json')

    assert response.status_code == 400

def test_signin_missing_field(test_client):
    """
    test returns 400 error for missing fields
    """
    response = test_client.post('/api/v2/auth/signin', data=json.dumps(DATA[8]),
                                content_type='application/json')

    assert response.status_code == 400
    