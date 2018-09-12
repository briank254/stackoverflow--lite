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