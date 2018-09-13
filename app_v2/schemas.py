"""
API schemas
"""

SIGNUP_SCHEMA  = {
    "type": "object",
    "properties": {
        "first_name": {"type":"string"},
        "last_name": {"type":"string"},
        "email": {"type":"string"},
        "password": {"type":"string"},
        "confirm_password": {"type":"string"}
    },
    
    "required": ["first_name", 
                 "last_name",
                 "email",
                 "password",
                 "confirm_password"    
                ]
}

SIGNIN_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"}
    },
    "required":['email', 'password']
}

QUESTION_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "question": {"type": "string"}
        
    },
    "required": ["title", "question"]
}
ANSWER_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
    
        
    },
    "required": ["answer"]
}


RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"enum": ["accepted", "rejected"]}
    },
    "required": ["status"]
}