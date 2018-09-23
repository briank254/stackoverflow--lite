"""initializes app as a module"""

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from . import routes

app.config.from_object('config')

if __name__ == "__main__":
    app.run(debug=True)
