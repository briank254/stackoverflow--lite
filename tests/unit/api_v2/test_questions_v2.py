"""
Tests for questions endpoint
"""
import json
import psycopg2
from flask import current_app

DATA = {'title':'Heroku', 'question':'How do I host my app on Heroku?'}

BAD_DATA = [{'title':'Heroku', 'question':''},
            {'title':'', 'question':'How do I host my app on Heroku?'},
            {'title':'Heroku'},
            {'question':'How do I host my app on Heroku?'}
           ]

def get_authentication_headers(test_client):
    """
    get headers for user authentication
    """
    ############### FIRST USER ########################

    user = {'first_name':'Kunihiko',
            'last_name': 'Kawani',
            'email': 'kawa@gmail.com', 
            'password':"password1234", 
            'confirm_password':"password1234"
           }

    test_client.post('/api/v2/auth/signup',
                     data=json.dumps(user),
                     content_type='application/json'
                    )

    signin_data = {'email': 'kawa@gmail.com', 
                  'password':"password1234"
                  }

    response = test_client.post('/api/v2/auth/signin', 
                                 data=json.dumps(signin_data),
                                 content_type='application/json'
                                )

    result = json.loads(response.data.decode('utf8'))
    headers = result['access_token']
    authentication_header1 = 'Bearer '+headers

    ############## SECOND USER 2 ###############################

    user_2 = {'first_name':'Samurai', 
              'last_name': 'Warr',
              'email': 'samwarr@gmail.com', 
              'password':"password123", 
              "confirm_password":"password123"}

    test_client.post('/api/v2/auth/signup', 
                     data=json.dumps(user_2),
                     content_type='application/json'
                    )

    signin_data2 = {'email': 'samwarr@gmail.com', 
                    'password':"password123"
                   }

    response2 = test_client.post('/api/v2/auth/signin', 
                                 data=json.dumps(signin_data2),
                                 content_type='application/json'
                                )

    result2 = json.loads(response2.data.decode('utf8'))
    headers2 = result2['access_token']
    authentication_header2 = 'Bearer '+headers2

    authentication_headers = [authentication_header1, authentication_header2]

    return authentication_headers

def get_question_id(test_client):
    """
    Returns id of a question for testing
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.get('/api/v2/questions', 
                               headers={'Authorization':authentication_header},
                               content_type='application/json'
                              )
    result = json.loads(response.data.decode('utf8'))

    question_id = result['questions'][0]['id']

    return question_id

####################################################################################

def test_get_questions(test_client):
    """
    test user can view questions
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.get('/api/v2/questions', 
                               headers={'Authorization':authentication_header},
                               content_type='application/json'
                              )
    
    assert response.status_code == 200

    result = json.loads(response.data.decode('utf8'))
    
    return result

def test_unauthenticated_user_views_questions(test_client):
    """
    test that unauthenticated user can view questions
    """
    response = test_client.get('/api/v2/questions')

    assert response.status_code == 200

    result = json.loads(response.data.decode('utf8'))

    return result

def test_post_question(test_client):
    """
    test that a user with car can create questions
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.post('/api/v2/questions', headers={'Authorization':authentication_header},
                                data=json.dumps(DATA), content_type='application/json')
    print (response.data)
    assert response.status_code == 201

def test_create_empty_string_question(test_client):
    """
    test that it returns 400 error
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.post('/api/v2/questions', headers={'Authorization':authentication_header},
                                data=json.dumps(BAD_DATA[0]), content_type='application/json')

    assert response.status_code == 400

def test_create_empty_string_title(test_client):
    """
    test that it returns 400 error
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.post('/api/v2/questions', headers={'Authorization':authentication_header},
                                data=json.dumps(BAD_DATA[1]), content_type='application/json')

    assert response.status_code == 400



def test_create_question_missing_field(test_client):
    """
    test returns 400 error if a field is missing
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.post('/api/v2/questions', headers={'Authorization':authentication_header},
                                data=json.dumps(BAD_DATA[2]), content_type='application/json')

    assert response.status_code == 400

def test_create_title_missing_field(test_client):
    """
    test returns 400 error if a field is missing
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.post('/api/v2/questions', headers={'Authorization':authentication_header},
                                data=json.dumps(BAD_DATA[3]), content_type='application/json')

    assert response.status_code == 400


def test_get_single_question(test_client):
    """
    test user can view details of single question
    """
    question_id = get_question_id(test_client)
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.get('/api/v2/questions/'+str(question_id), 
                               headers={'Authorization':authentication_header},
                               content_type='application/json')

    assert response.status_code == 200


def test_non_existent_question(test_client):
    """
    test that requesting for none existent question raises 404 error
    """
    authentication_header = get_authentication_headers(test_client)[0]
    response = test_client.get('/api/v2/questions/50000', headers={'Authorization':authentication_header},
                               content_type='application/json')

    assert response.status_code == 404
