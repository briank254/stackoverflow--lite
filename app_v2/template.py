'''
Swagger template
'''

TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Stackoverflow-Lite",
        "description": 'StackOverflow--lite is a platform where people \
                        can ask questions and provide answers',

    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
    "definitions": {
        "UserSignup": {
            "type": "object",
            "properties": {
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string"},
                "confirm_password": {"type": "string"}
            }

        },

        "UserSignin": {
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "password": {"type": "string"}
            }

        },

        "Questions": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "question": {"type": "string"}

            }

        },
        "Question_details": {
            "type": "object",
            "properties": {
                "question_id": {"type": "number"},
                "title": {"type": "string"},
                "question": {"type": "string"}

            }

        },
        "Answers": {
            "type": "object",
            "properties": {
                "answer": {"type": "string"},


            }

        },
        "Response": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["rejected", "accepted"]}
            }


        }
    }
}
