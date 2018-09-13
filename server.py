"""
v2 application entry point
"""
import os
from app_v2 import create_app

APP = create_app(os.getenv('FLASK_ENV'))

if __name__ == '__main__':
    APP.run()
    