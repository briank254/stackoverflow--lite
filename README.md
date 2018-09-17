[![Build Status](https://travis-ci.org/graycadeau/stackoverflow--lite.svg?branch=develop)](https://travis-ci.org/graycadeau/stackoverflow--lite) 
[![Coverage Status](https://coveralls.io/repos/github/graycadeau/stackoverflow--lite/badge.svg?branch=develop)](https://coveralls.io/github/graycadeau/stackoverflow--lite?branch=develop)

# stackoverflow--lite
StackOverflow--lite is a platform where people can ask questions and provide answers. 

# Installation - UI
To get a view of the front-end UI, do the following:&nbsp;

Clone the repository into your local environment: &nbsp;
`git clone https://github.com/graycadeau/stackoverflow--lite.git`&nbsp;

Switch to stackoverflow-lite directory you just cloned:&nbsp;
`cd stackoverflow--lite/UI`&nbsp;

Run `index.html` file in your browser.&nbsp;

#### UI link to gh-pages:
https://graycadeau.github.io/stackoverflow--lite/

# Installation - API 

#### Requirements
Recommended set up on your local environment before getting started

1. python 3
2. Git
3. Working browser or Postman
4. virtualenv for an isolated working environment. 

Do the following:

* Clone the repo from local terminal into a folder of your choice: 
```
git clone https://github.com/graycadeau/stackoverflow--lite.git
``` 

* Navigate to the cloned folder 
```
cd stackoverflow--lite
```

* Create a `.env` file with same format as in `.env .example` and run it 
```
source .env
```
* Install all dependencies

```
pip install -r requirements.txt
```
* Run the Flask application
```
flask run
```
# Testing
To test run the command 
```
pytest
```
# Endpoints

Endpoint | Functionality 
------------ | -------------
POST   /api/v1/questions | Post a qusetion
GET   /api/v1/questions | Get all questions
GET   /api/v1/questions/<question_id> | Get a single question
DELETE   /api/v1/questions/<question_id> | Delete a question
POST   /api/v1/questions/<question_id>/answers | Post an answer to a question
GET   /api/v1/questions/<question_id>/answers | Get all answers to a question
PUT   /api/v1/questions/<question_id>/answers/<question_id> | Update an answer to a question

# Test API endpoints
Fire up Postman to test the endpoints. 
