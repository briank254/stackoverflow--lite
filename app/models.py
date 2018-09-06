"""app models"""

USERS = []

class User:
    def __init__(self, name, email, password):

        """class constructor"""

        self.name = name
        self.email = email
        self.password = password

    def add(self):

        """method to add new user to users"""
        USERS.append(self)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
